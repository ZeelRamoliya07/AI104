"""
Write a class called Password_manager. The class should have a list called old_passwords that
holds all of the user’s past passwords. The last item of the list is the user’s current pass word.
There should be a method called get_password that returns the current password and a method
called set_password that sets the user’s password. The set_password method should only
change the password if the attempted password is different from all the user’s past passwords.
Finally, create a method called is_correct that receives a string and returns a boolean True or
False depending on whether the string is equal to the current password or not.
"""

class PasswordManager:
    def __init__(self):
        self.old_passwords = [] 

    def get_password(self):
        return self.old_passwords[-1]

    def set_password(self, new_password):
        if len(new_password) < 6:
            print("Error: Password must be at least 6 characters long.")
            return
        if new_password not in self.old_passwords:
            self.old_passwords.append(new_password)
            print("Password updated successfully!")
        else:
            print("Error: Password has been used before.")

    def is_correct(self, password):
        return password == self.get_password()

def password_manager_menu():
    pm = PasswordManager()
    while True:
        print("\nPassword Manager:")
        print("1. Set Password")
        print("2. Get Current Password")
        print("3. Check Password")
        print("4. Exit")
        choice = input("Enter your choice: ")
        
        if choice == '1':
            new_pass = input("Enter new password (at least 6 characters): ")
            pm.set_password(new_pass)
        elif choice == '2':
            print("Current Password:", pm.get_password())
        elif choice == '3':
            check_pass = input("Enter password to check: ")
            print("Correct Password:" if pm.is_correct(check_pass) else "Incorrect Password")
        elif choice == '4':
            break
        else:
            print("Invalid choice, try again.")


password_manager_menu()
