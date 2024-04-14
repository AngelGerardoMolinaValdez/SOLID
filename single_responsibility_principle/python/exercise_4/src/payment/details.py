from dataclasses import dataclass

@dataclass
class PaymentDetails:
    """
    PaymentDetails class is a data class that holds the payment details
    for a payment transaction.

    Attributes:
    amount: float -- The amount of the payment. Example: 100.00
    currency: str -- The currency of the payment. Example: USD
    card_number: str -- The card number. Example: 4111111111111111
    card_holder: str -- The card holder name. Example: John Doe
    card_expiration: str -- The card expiration date. Example: 12/25
    card_cvv: str -- The card cvv. Example: 123
    card_type: str -- The card type. Example: visa
    """
    amount: float
    currency: str
    card_number: str
    card_holder: str
    card_expiration: str
    card_cvv: str
    card_type: str

@dataclass
class UserDetails:
    """
    User class is a data class that holds the user details.

    Attributes:
    id: int -- The user id. Example: 1
    name: str -- The user name. Example: John Doe
    email: str -- The user email. Example: john_doe@mail.com
    """
    id: str
    name: str
    email: str
