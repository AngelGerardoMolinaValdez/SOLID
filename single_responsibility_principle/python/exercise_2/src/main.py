
from validations.add_user_validation import AddUserValidation
from validations.update_user_validation import UpdateUserValidation
from user_manager import UserManager

if __name__ == "__main__":
    add_user_validation = AddUserValidation()
    update_user_validation = UpdateUserValidation()
    user_manager = UserManager()

    user_manager.add_user(add_user_validation, "user1")
    user_manager.update_user(update_user_validation, "user2")
