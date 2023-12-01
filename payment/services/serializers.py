import stripe

from config import settings

stripe.api_key = settings.STRIPE_SECRET_KEY


def create_product(obj):
    """{
  "active": true,
  "attributes": [],
  "created": 1701377831,
  "default_price": null,
  "description": "$12/Month subscription",
  "features": [],
  "id": "prod_P6UG5zOiIIC8hc",
  "images": [],
  "livemode": false,
  "metadata": {},
  "name": "\u0425\u0438\u043c\u0438\u044f.\u0410\u043d\u0430\u0431\u043e\u043b\u0438\u043a\u0438",
  "object": "product",
  "package_dimensions": null,
  "shippable": null,
  "statement_descriptor": null,
  "tax_code": null,
  "type": "service",
  "unit_label": null,
  "updated": 1701377831,
  "url": null
}"""
    starter_subscription = stripe.Product.create(
        name=obj.course.name,
        description=obj.course.description,
    )
    return starter_subscription['id']


def create_price(amount, id_product):
    """
    {
  "active": true,
  "billing_scheme": "per_unit",
  "created": 1701377937,
  "currency": "usd",
  "custom_unit_amount": null,
  "id": "price_1OIHK1LQzeH0FdNv2C4IYC9a",
  "livemode": false,
  "lookup_key": null,
  "metadata": {},
  "nickname": null,
  "object": "price",
  "product": "prod_P6UG5zOiIIC8hc",
  "recurring": {
    "aggregate_usage": null,
    "interval": "month",
    "interval_count": 1,
    "trial_period_days": null,
    "usage_type": "licensed"
  },
  "tax_behavior": "unspecified",
  "tiers_mode": null,
  "transform_quantity": null,
  "type": "recurring",
  "unit_amount": 200,
  "unit_amount_decimal": "200"
}
    """
    starter_subscription_price = stripe.Price.create(
        unit_amount=amount,
        currency="usd",
        recurring={"interval": "month"},
        product=id_product,
    )
    return starter_subscription_price['id']


def create_sessions(id_price):
    url = stripe.checkout.Session.create(
        success_url="https://example.com/success",
        line_items=[
            {
                "price": id_price,
                "quantity": 1,
            },
        ],
        mode="subscription",
    )
    return url['url']


def retrieve_intent():
    retrieve_pay = stripe.PaymentIntent.retrieve()
    return retrieve_pay


# @csrf_exempt
# def create_payment(obj):
#     stripe.api_key = settings.STRIPE_SECRET_KEY
#     # Create a PaymentIntent with the order amount and currency
#     intent = stripe.PaymentIntent.create(
#         amount=obj.sum_of_pay,
#         currency='usd',
#         # In the latest version of the API, specifying the `automatic_payment_methods` parameter is optional because Stripe enables its functionality by default.
#         automatic_payment_methods={
#             'enabled': True,
#         },
#         receipt_email=obj.user
#     )
#     # return intent['id']
#     return intent

# def webhook():
#     web_hook = stripe.WebhookEndpoint.create(
#         url="https://example.com/my/webhook/endpoint",
#         enabled_events=[
#             "charge.failed",
#             "charge.succeeded",
#         ],
#     )
#     return web_hook
