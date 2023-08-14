import stripe

from .base import stripe_method
from .stripe_err_handler import stripe_error_handler


@stripe_method
def create_setup_intent(customer_id, confirm=False, **kwargs):
    try:
        setup_intent = stripe.SetupIntent.create(
            customer=customer_id,
            confirm=confirm,
            **kwargs,
        )
        return setup_intent
    except stripe.error.StripeError as e:
        stripe_error_handler(e)


@stripe_method
def confirm_setup_intent(setup_intent_id, **kwargs):
    try:
        setup_intent = stripe.SetupIntent.confirm(
            setup_intent_id,
            **kwargs,
        )
        return setup_intent
    except stripe.error.StripeError as e:
        stripe_error_handler(e)
