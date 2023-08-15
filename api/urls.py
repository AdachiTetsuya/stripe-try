from django.urls import path, include
from api.views import ChapterViewSet, CardViewSet
from rest_framework import routers

router = routers.DefaultRouter()

router.register("chapters", ChapterViewSet, basename="chapters")
router.register("cards", CardViewSet, basename="cards")

urlpatterns = [
    path("", include(router.urls)),
]