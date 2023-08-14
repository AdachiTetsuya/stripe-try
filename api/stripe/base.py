from django.conf import settings

import stripe


def stripe_method(func):
    def wrapper(*args, **kwargs):
        stripe.api_key = settings.STRIPE_SECRET_KEY
        if hasattr(settings, "STRIPE_API_HOST") and settings.STRIPE_API_HOST:
            stripe.api_base = settings.STRIPE_API_HOST
        return func(*args, **kwargs)

    return wrapper
