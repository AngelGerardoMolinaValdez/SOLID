from unittest import TestCase
import re
import sys

sys.path.append("src")

from src.payment.report import PaymentReportHtml, PaymentReportPdf, PaymentReportPlainText
from src.payment.details import PaymentDetails, UserDetails

class TestReportPayment(TestCase):
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
    
    def test_payment_report_pdf(self):
        pdf_report = PaymentReportPdf()

        pattern = re.compile(r"pdf report generated with data: .+ and .+")
        self.assertTrue(pattern.match(pdf_report.generate(self.payment_details, self.user_details)))
    
    def test_payment_report_html(self):
        html_report = PaymentReportHtml()

        pattern = re.compile(r"html report generated with data: .+ and .+")
        self.assertTrue(pattern.match(html_report.generate(self.payment_details, self.user_details)))
    
    def test_payment_report_plain_text(self):
        plain_text_report = PaymentReportPlainText()

        pattern = re.compile(r"plain text report generated with data: .+ and .+")
        self.assertTrue(pattern.match(plain_text_report.generate(self.payment_details, self.user_details)))
