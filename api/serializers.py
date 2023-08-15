from rest_framework import serializers
from api.models import User, Chapter, Card, PurchaseLog

class ChapterSerializer(serializers.ModelSerializer):
    is_locked = serializers.BooleanField(default=True, required=False)

    class Meta:
        model = Chapter
        fields = (
            "id",
            "title",
            "is_free",
            "product_id",
            "price_id",
            "price",
            "is_locked",
        )


class CardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Card
        exclude = ("user",)

class PurchaseLogSerializer(serializers.ModelSerializer):
    class Meta:
        model = PurchaseLog
        exclude = ("user",)