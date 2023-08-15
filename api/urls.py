from django.urls import path, include
from api.views import ChapterViewSet, CardViewSet, PaymentIntent,PurchaseLogViewSet
from rest_framework import routers


router = routers.DefaultRouter()

router.register("chapters", ChapterViewSet, basename="chapters")
router.register("cards", CardViewSet, basename="cards")
router.register("purchase", PurchaseLogViewSet, basename="purchase")

urlpatterns = [
    path("", include(router.urls)),
    path("payment-intent/", PaymentIntent.as_view(), name="line"),
]