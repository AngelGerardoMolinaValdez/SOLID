from .base import PaymentGateway
from .details import PaymentDetails, UserDetails

class PaymentGatewayPaypal(PaymentGateway):
    """Payment gateway for paypal."""

    def process(self, payment_details: PaymentDetails, user_details: UserDetails) -> str:
        """Process the payment."""
        return "paypal payment processed successfully with data: " + str(payment_details) + " and " + str(user_details)

class PaymentGatewayStripe(PaymentGateway):
    """Payment gateway for stripe."""

    def process(self, payment_details: PaymentDetails, user_details: UserDetails) -> str:
        """Process the payment."""
        return "stripe payment processed successfully with data: " + str(payment_details) + " and " + str(user_details)

class PaymentGatewayRazorpay(PaymentGateway):
    """Payment gateway for razorpay."""

    def process(self, payment_details: PaymentDetails, user_details: UserDetails) -> str:
        """Process the payment."""
        return "razorpay payment processed successfully with data: " + str(payment_details) + " and " + str(user_details)
