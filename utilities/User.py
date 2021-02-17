class User:
    def __init__(self, username, first_name, last_name, email, address, password):
        self.username = username
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.address = address
        self.password = password

    @property
    def user_name(self):
        return self.first_name + ' ' + self.last_name

    @property
    def user_address(self):
        return self.user_name + " lives at " + self.address
