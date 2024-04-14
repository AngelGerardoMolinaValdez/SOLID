from abc import ABC, abstractmethod
from .details import PaymentDetails, UserDetails

class PaymentGateway(ABC):
    """Base class for payment gateway."""

    @abstractmethod
    def process(self, payment_details: PaymentDetails, user_details: UserDetails) -> str:
        """Process the payment."""
        pass

class PaymentReport(ABC):
    """Base class for payment report."""

    @abstractmethod
    def generate(self, payment_details: PaymentDetails, user_details: UserDetails) -> str:
        """Generate the payment report."""
        pass
