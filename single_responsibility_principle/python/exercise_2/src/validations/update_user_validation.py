from validations.validation import Validation

class UpdateUserValidation(Validation):
    def validate(self, value: str) -> bool:
        """ method to validate a value"""
        return len(value) > 0