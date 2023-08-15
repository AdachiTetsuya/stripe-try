from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    username = models.CharField("ユーザー名", max_length=30, blank=True, null=True)
    email = models.EmailField("メールアドレス", unique=True)
    customer_id = models.CharField("StripeCustomerId", max_length=50, blank=True, null=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username"]


class Chapter(models.Model):
    title = models.CharField("タイトル", max_length=100)
    is_free = models.BooleanField("無料かどうか", default=True)
    product_id = models.CharField("StripeProductId", max_length=50, blank=True, null=True)
    price_id = models.CharField("StripePriceId", max_length=50, blank=True, null=True)
    price = models.IntegerField("価格", default=0)


class Card(models.Model):
    card_number = models.CharField("カード番号下四桁", max_length=4)
    ex_year = models.CharField("カード有効期限(年)", max_length=2)
    ex_month = models.CharField("カード有効期限(月)", max_length=2)
    user = models.ForeignKey(
        User, verbose_name="所有ユーザー", related_name="user_card", on_delete=models.CASCADE
    )
    payment_method_id = models.CharField("PaymentMethodId", max_length=50, blank=True, null=True)

    def __str__(self):
        return self.user.username

    class Meta:
        verbose_name = "カード情報"


class PurchaseLog(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.SET_NULL, verbose_name="ユーザー", null=True, blank=True
    )
    chapter = models.ForeignKey(Chapter, on_delete=models.SET_NULL, verbose_name="ユーザー", null=True, blank=True)
    price = models.IntegerField("取引金額", blank=True, null=True)
    created_at = models.DateTimeField("作成日時", auto_now_add=True)

    class Meta:
        verbose_name = "決済ログ"

    def __str__(self):
        return self.user.username
