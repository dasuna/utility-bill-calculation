from __future__ import absolute_import, division, print_function

import stripe
from stripe.test.helper import StripeResourceTest


DUMMY_INVOICE_ITEM = {
    'amount': 456,
    'currency': 'usd',
}


class InvoiceTest(StripeResourceTest):

    def test_add_invoice_item(self):
        customer = stripe.Customer(id="cus_invoice_items")
        customer.add_invoice_item(**DUMMY_INVOICE_ITEM)

        expected = DUMMY_INVOICE_ITEM.copy()
        expected['customer'] = 'cus_invoice_items'

        self.requestor_mock.request.assert_called_with(
            'post',
            '/v1/invoiceitems',
            expected,
            None,
        )

    def test_retrieve_invoice_items(self):
        customer = stripe.Customer(id="cus_get_invoice_items")
        customer.invoice_items()

        self.requestor_mock.request.assert_called_with(
            'get',
            '/v1/invoiceitems',
            {'customer': 'cus_get_invoice_items'},
        )

    def test_convert_to_stripe_object(self):
        item = stripe.util.convert_to_stripe_object({
            'id': 'ii_foo',
            'object': 'invoiceitem',
        })
        self.assertIsInstance(item, stripe.InvoiceItem)

    def test_invoice_create(self):
        customer = stripe.Customer(id="cus_invoice")
        stripe.Invoice.create(customer=customer.id)

        self.requestor_mock.request.assert_called_with(
            'post',
            '/v1/invoices',
            {
                'customer': 'cus_invoice',
            },
            None
        )

    def test_retrieve_customer_invoices(self):
        customer = stripe.Customer(id="cus_invoice_items")
        customer.invoices()

        self.requestor_mock.request.assert_called_with(
            'get',
            '/v1/invoices',
            {
                'customer': 'cus_invoice_items',
            },
        )

    def test_pay_invoice(self):
        invoice = stripe.Invoice(id="ii_pay")
        invoice.pay()

        self.requestor_mock.request.assert_called_with(
            'post',
            '/v1/invoices/ii_pay/pay',
            {},
            None
        )

    def test_pay_invoice_params(self):
        invoice = stripe.Invoice(id="ii_pay")
        invoice.pay(source="src_foo")

        self.requestor_mock.request.assert_called_with(
            'post',
            '/v1/invoices/ii_pay/pay',
            {
                'source': 'src_foo',
            },
            None
        )

    def test_upcoming_invoice(self):
        stripe.Invoice.upcoming()

        self.requestor_mock.request.assert_called_with(
            'get',
            '/v1/invoices/upcoming',
            {},
        )

    def test_upcoming_invoice_subscription_items(self):
        stripe.Invoice.upcoming(subscription_items=[
            {"plan": "foo", "quantity": 3}
        ])
        self.requestor_mock.request.assert_called_with(
            'get',
            '/v1/invoices/upcoming',
            {
                'subscription_items': {
                    "0": {
                        "plan": "foo",
                        "quantity": 3,
                    },
                },
            },
        )
