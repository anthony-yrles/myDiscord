
class Authentication:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def authenticate(self):
        if self.username == "admin" and self.password == "admin":
            return True
        else:
            return False
        
    def login(self):
        if self.authenticate():
            return "Login successful"
        else:
            return "Login failed"
    
    def logout(self):
        return "Logout successful"
    
    def creation_account(self):
        return "Account created"
    
    def test_name(self):
        if self.username == "admin":
            return "Username already taken"
        else:
            return "Username available"
        
    def test_password(self):
        if self.password == "admin":
            return "Password already taken"
        else:
            return "Password available"
        
    def change_password(self, new_password):
        self.password = new_password
        return "Password changed"
    

# Test
auth = Authentication("admin", "admin")
print(auth.login())  # Login successful
print(auth.logout())  # Logout successful
print(auth.creation_account())  # Account created
print(auth.test_name())  # Username already taken
print(auth.test_password())  # Password already taken
print(auth.change_password("admin123"))  # Password changed

