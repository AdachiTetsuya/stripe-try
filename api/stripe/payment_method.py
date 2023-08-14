import stripe

from .base import stripe_method
from .stripe_err_handler import stripe_error_handler


@stripe_method
def create_payment_method(type, **kwargs):
    try:
        payment_method = stripe.PaymentMethod.create(
            type=type,
            **kwargs,
        )
        return payment_method
    except stripe.error.StripeError as e:
        stripe_error_handler(e)


@stripe_method
def retrieve_payment_method(payment_method_id, **kwargs):
    try:
        payment_method = stripe.PaymentMethod.retrieve(
            payment_method_id,
            **kwargs,
        )
        return payment_method
    except stripe.error.StripeError as e:
        stripe_error_handler(e)


@stripe_method
def list_customer_payment_method(customer_id, **kwargs):
    try:
        payment_method_list = stripe.PaymentMethod.list_payment_methods(
            customer_id,
            **kwargs,
        )
        return payment_method_list
    except stripe.error.StripeError as e:
        stripe_error_handler(e)


@stripe_method
def attach_payment_method_customer(payment_method_id, customer_id, **kwargs):
    try:
        payment_method = stripe.PaymentMethod.attach(
            payment_method_id, customer=customer_id, **kwargs
        )
        return payment_method
    except stripe.error.StripeError as e:
        stripe_error_handler(e)


@stripe_method
def detach_payment_method_customer(payment_method_id, **kwargs):
    try:
        payment_method = stripe.PaymentMethod.detach(payment_method_id, **kwargs)
        return payment_method
    except stripe.error.StripeError as e:
        stripe_error_handler(e)
