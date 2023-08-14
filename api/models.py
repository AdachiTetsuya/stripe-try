from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    username = models.CharField("ユーザー名", max_length=30, blank=True, null=True)
    email = models.EmailField("メールアドレス", unique=True)
    customer_id = models.CharField("StripeCustomerId", max_length=50, blank=True, null=True)
    
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username"]

