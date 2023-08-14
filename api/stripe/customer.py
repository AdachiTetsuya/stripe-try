import stripe

from .base import stripe_method
from .stripe_err_handler import stripe_error_handler


@stripe_method
def create_customer(**kwargs):
    try:
        customer = stripe.Customer.create(
            **kwargs,
        )
        return customer
    except stripe.error.StripeError as e:
        stripe_error_handler(e)


@stripe_method
def update_customer(customer_id, **kwargs):
    try:
        customer = stripe.Customer.modify(
            customer_id,
            **kwargs,
        )
        return customer
    except stripe.error.StripeError as e:
        stripe_error_handler(e)


@stripe_method
def retrieve_customer(customer_id):
    try:
        customer = stripe.Customer.retrieve(
            customer_id,
        )
        return customer
    except stripe.error.StripeError as e:
        stripe_error_handler(e)


@stripe_method
def delete_customer(customer_id):
    try:
        stripe.Customer.delete(
            customer_id,
        )
    except stripe.error.StripeError as e:
        stripe_error_handler(e)
