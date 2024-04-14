from payment.process import PaymentGatewayPaypal, PaymentGatewayStripe, PaymentGatewayRazorpay
from payment.report import PaymentReportPdf, PaymentReportHtml, PaymentReportPlainText
from payment.details import PaymentDetails, UserDetails

def main() -> None:
    payment_details = PaymentDetails(
        amount=100.00,
        currency="USD",
        card_number="4111111111111111",
        card_holder="John Doe",
        card_expiration="12/25",
        card_cvv="123",
        card_type="visa"
    )

    user_details = UserDetails(
        id="1",
        name="John Doe",
        email="john_doe@mail.com"
    )

    paypal = PaymentGatewayPaypal()
    stripe = PaymentGatewayStripe()
    razorpay = PaymentGatewayRazorpay()

    pdf_report = PaymentReportPdf()
    html_report = PaymentReportHtml()
    plain_text_report = PaymentReportPlainText()

    print(paypal.process(payment_details, user_details))
    print(stripe.process(payment_details, user_details))
    print(razorpay.process(payment_details, user_details))

    print(pdf_report.generate(payment_details, user_details))
    print(html_report.generate(payment_details, user_details))
    print(plain_text_report.generate(payment_details, user_details))

if __name__ == "__main__":
    main()
