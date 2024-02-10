from validations.validation import Validation

class UserManager:
    def add_user(self, validation: Validation, username: str) -> bool:
        """ method to add a user"""
        if not validation.validate(username):
            print("ERROR: usuario no valido para agregar")
        else:
            print(f"se agrego correctamente {username}")

    def update_user(self, validation: Validation, username: str) -> bool:
        """ method to update a user"""
        if not validation.validate(username):
            print("ERROR: usuario no valido para actualizar")
        else:
            print(f"se actualizo correctamente {username}")

        