import stripe

from .base import stripe_method
from .stripe_err_handler import stripe_error_handler


@stripe_method
def create_payment_intent(amount, currency="jpy", confirm=False, **kwargs):
    print(kwargs)
    try:
        payment_intent = stripe.PaymentIntent.create(
            amount=amount,
            currency=currency,
            confirm=confirm,
            **kwargs,
        )
        return payment_intent
    except stripe.error.StripeError as e:
        stripe_error_handler(e)


@stripe_method
def confirm_payment_intent(payment_intent_id, **kwargs):
    try:
        payment_intent = stripe.PaymentIntent.confirm(
            payment_intent_id,
            **kwargs,
        )
        return payment_intent
    except stripe.error.StripeError as e:
        stripe_error_handler(e)


@stripe_method
def cancel_payment_intent(payment_intent_id, **kwargs):
    try:
        payment_intent = stripe.PaymentIntent.cancel(
            payment_intent_id,
            **kwargs,
        )
        return payment_intent
    except stripe.error.StripeError as e:
        stripe_error_handler(e)
