import stripe

from .base import stripe_method
from .stripe_err_handler import stripe_error_handler


@stripe_method
def create_product(name, **kwargs):
    try:
        product = stripe.Product.create(
            name=name,
            **kwargs,
        )
        return product
    except stripe.error.StripeError as e:
        stripe_error_handler(e)


@stripe_method
def update_product(product_id, **kwargs):
    try:
        product = stripe.Product.modify(
            product_id,
            **kwargs,
        )
        return product
    except stripe.error.StripeError as e:
        stripe_error_handler(e)


@stripe_method
def retrieve_product(product_id):
    try:
        product = stripe.Product.retrieve(
            product_id,
        )
        return product
    except stripe.error.StripeError as e:
        stripe_error_handler(e)


@stripe_method
def delete_product(product_id):
    try:
        stripe.Product.delete(
            product_id,
        )
    except stripe.error.StripeError as e:
        stripe_error_handler(e)
