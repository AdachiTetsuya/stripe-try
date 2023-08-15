from django.http.response import JsonResponse
from rest_framework import viewsets
from rest_framework.decorators import api_view
from api.models import User, Chapter, Card, PurchaseLog
from api.serializers import ChapterSerializer, CardSerializer, PurchaseLogSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import ValidationError
from api.stripe.customer import create_customer, update_customer
from api.stripe.payment_method import attach_payment_method_customer
from api.stripe.payment_intent import create_payment_intent
from api.stripe.stripe_err_handler import StripeHandledError
from api.stripe.price import retrieve_price

class ChapterViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Chapter.objects.all()
    serializer_class = ChapterSerializer
    filterset_fields = ["id"]


class CardViewSet(viewsets.ModelViewSet):
    queryset = Card.objects.all()
    serializer_class = CardSerializer
    filterset_fields = ["id"]

    def __create_customer(self, user, payment_method_id):
        try:
            customer = create_customer(
                name=user.username,
                payment_method=payment_method_id,
                invoice_settings={
                    "default_payment_method": payment_method_id,
                },
            )
            user.customer_id = customer["id"]
            user.save()
            return customer
        except StripeHandledError as e:
            raise ValidationError({"non_field_errors": [str(e)]})

    def __update_customer(self, user, payment_method_id):
        try:
            customer = update_customer(
                user.customer_id,
                invoice_settings={
                    "default_payment_method": payment_method_id,
                },
            )
            return customer
        except StripeHandledError as e:
            raise ValidationError({"non_field_errors": [str(e)]})

    def __attach_payment_method_to_user(self, customer_id, payment_method_id):
        try:
            payment_method = attach_payment_method_customer(
                payment_method_id,
                customer_id,
            )
            return payment_method
        except StripeHandledError as e:
            raise ValidationError({"non_field_errors": [str(e)]})

    def __setup_stripe_customer(self, user, payment_method_id):
        if user.customer_id:
            self.__attach_payment_method_to_user(
                user.customer_id,
                payment_method_id,
            )
            self.__update_customer(user, payment_method_id)
        else:
            self.__create_customer(user, payment_method_id)

    def perform_create(self, serializer):
        user = self.request.user
        validated_data = serializer.validated_data
        payment_method_id = self.request.data["payment_method_id"]
        self.__setup_stripe_customer(user, payment_method_id)
        return serializer.save(
            user=user
        )
    

class PurchaseLogViewSet(viewsets.ModelViewSet):
    queryset = PurchaseLog.objects.all()
    serializer_class = PurchaseLogSerializer

    def __create_payment_intent(self, price, customer_id, payment_method_id):
        try:
            payment_intent = create_payment_intent(
                amount=price,
                confirm=True,
                customer=customer_id,
                payment_method=payment_method_id,
                automatic_payment_methods={
                    'enabled': True,
                    'allow_redirects': 'never'
                },
            )
            return payment_intent
        except StripeHandledError as e:
            raise ValidationError({"non_field_errors": [str(e)]})

    def perform_create(self, serializer):
        user = self.request.user
        validated_data = serializer.validated_data
        price_obj = retrieve_price(validated_data["chapter"].price_id)
        price = price_obj["unit_amount"]
        customer_id = user.customer_id
        payment_method_id = user.user_card.first().payment_method_id

        payment_intent = self.__create_payment_intent(price, customer_id, payment_method_id)
        return serializer.save(
            user=user,
            price=price
        )

    
class PaymentIntent(APIView):

    def post(self, request, *args, **kwargs):
        try:
            payment_intent = create_payment_intent(
                **request.data,
                automatic_payment_methods={
                    'enabled': True,
                },
            )
        except StripeHandledError as e:
            raise ValidationError({"non_field_errors": [str(e)]})
        return Response({"client_secret": payment_intent["client_secret"]})
        
    
