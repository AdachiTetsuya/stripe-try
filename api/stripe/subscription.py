import stripe

from .base import stripe_method
from .stripe_err_handler import stripe_error_handler


@stripe_method
def create_subscription(customer_id, price_id, **kwargs):
    try:
        subscription = stripe.Subscription.create(
            customer=customer_id,
            items=[
                {"price": price_id},
            ],
            **kwargs,
        )
        return subscription
    except stripe.error.StripeError as e:
        stripe_error_handler(e)


@stripe_method
def update_subscription(subsc_id, **kwargs):
    try:
        subscription = stripe.Subscription.modify(
            subsc_id,
            **kwargs,
        )
        return subscription
    except stripe.error.StripeError as e:
        stripe_error_handler(e)


@stripe_method
def retrieve_subscription(subsc_id):
    try:
        subscription = stripe.Subscription.retrieve(
            subsc_id,
        )
        return subscription
    except stripe.error.StripeError as e:
        stripe_error_handler(e)


@stripe_method
def cancel_subscription(subsc_id, **kwargs):
    try:
        subscription = stripe.Subscription.delete(
            subsc_id,
            **kwargs,
        )
        return subscription
    except stripe.error.StripeError as e:
        stripe_error_handler(e)
