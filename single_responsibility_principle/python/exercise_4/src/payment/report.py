from .base import PaymentReport
from .details import PaymentDetails, UserDetails

class PaymentReportPdf(PaymentReport):
    """Payment report for pdf."""

    def generate(self, payment_details: PaymentDetails, user_details: UserDetails) -> str:
        """Generate the payment report."""
        return "pdf report generated with data: " + str(payment_details) + " and " + str(user_details)

class PaymentReportHtml(PaymentReport):
    """Payment report for html."""

    def generate(self, payment_details: PaymentDetails, user_details: UserDetails) -> str:
        """Generate the payment report."""
        return "html report generated with data: " + str(payment_details) + " and " + str(user_details)

class PaymentReportPlainText(PaymentReport):
    """Payment report for plain text."""

    def generate(self, payment_details: PaymentDetails, user_details: UserDetails) -> str:
        """Generate the payment report."""
        return "plain text report generated with data: " + str(payment_details) + " and " + str(user_details)
