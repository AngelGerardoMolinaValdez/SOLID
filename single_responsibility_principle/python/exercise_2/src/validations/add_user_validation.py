from validations.validation import Validation

class AddUserValidation(Validation):
    def validate(self, value: str) -> bool:
        """ method to validate a value"""
        return len(value) > 0
