import stripe

from .base import stripe_method
from .stripe_err_handler import stripe_error_handler


@stripe_method
def create_price(product_id, unit_amount, currency="jpy", **kwargs):
    try:
        price = stripe.Price.create(
            product=product_id,
            unit_amount=unit_amount,
            currency=currency,
            **kwargs,
        )
        return price
    except stripe.error.StripeError as e:
        stripe_error_handler(e)


@stripe_method
def update_price(price_id, **kwargs):
    try:
        price = stripe.Price.modify(
            price_id,
            **kwargs,
        )
        return price
    except stripe.error.StripeError as e:
        stripe_error_handler(e)


@stripe_method
def retrieve_price(price_id):
    try:
        price = stripe.Price.retrieve(
            price_id,
        )
        return price
    except stripe.error.StripeError as e:
        stripe_error_handler(e)


@stripe_method
def delete_price(price_id):
    try:
        stripe.Price.delete(
            price_id,
        )
    except stripe.error.StripeError as e:
        stripe_error_handler(e)
