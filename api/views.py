from django.http.response import JsonResponse
from rest_framework import viewsets
from rest_framework.decorators import api_view
from api.models import User, Chapter, Card, PaymentLog
from api.serializers import ChapterSerializer, CardSerializer


class ChapterViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Chapter.objects.all()
    serializer_class = ChapterSerializer
    filterset_fields = ["id"]


class CardViewSet(viewsets.ModelViewSet):
    queryset = Card.objects.all()
    serializer_class = CardSerializer
    filterset_fields = ["id"]

    def perform_create(self, serializer):
        validated_data = serializer.validated_data
        return serializer.save(
            user=self.request.user
        )