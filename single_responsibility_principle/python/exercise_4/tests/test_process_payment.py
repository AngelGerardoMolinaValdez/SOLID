from unittest import TestCase
import re
import sys

sys.path.append("src")

from src.payment.process import PaymentGatewayPaypal, PaymentGatewayStripe, PaymentGatewayRazorpay
from src.payment.details import PaymentDetails, UserDetails

class TestProcessPayment(TestCase):
    payment_details = None
    user_details = None

    @classmethod
    def setUpClass(cls):
        cls.payment_details = PaymentDetails(
            amount=100.00,
            currency="USD",
            card_number="4111111111111111",
            card_holder="John Doe",
            card_expiration="12/25",
            card_cvv="123",
            card_type="visa"
        )

        cls.user_details = UserDetails(
            id="1",
            name="John Doe",
            email="john_doe@mail.com"
        )

    def test_payment_gateway_paypal(self):
        paypal = PaymentGatewayPaypal()

        pattern = re.compile(r"paypal payment processed successfully with data: .+ and .+")
        self.assertTrue(pattern.match(paypal.process(self.payment_details, self.user_details)))
    
    def test_payment_gateway_stripe(self):
        stripe = PaymentGatewayStripe()

        pattern = re.compile(r"stripe payment processed successfully with data: .+ and .+")
        self.assertTrue(pattern.match(stripe.process(self.payment_details, self.user_details)))
    
    def test_payment_gateway_razorpay(self):
        razorpay = PaymentGatewayRazorpay()

        pattern = re.compile(r"razorpay payment processed successfully with data: .+ and .+")
        self.assertTrue(pattern.match(razorpay.process(self.payment_details, self.user_details)))
