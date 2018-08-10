# -*- coding: UTF-8 -*-
class Privileges():
    def __init__(self, privileges=["can add post", "can delete post", "can ban user"]):
        self.privileges = privileges

    def show_privileges(self):
        for self.privilege in self.privileges:
            print(self.privilege)


class User():
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.login_attemps = 0

    def describe_user(self):
        print('First name: ' + self.first_name.title())
        print('Last name: ' + self.last_name.title())

    def greet_user(self):
        print("Hello," + self.first_name.title() + ' ' + self.last_name.title() + '!')

    def increment_login_attemps(self):
        self.login_attemps += 1

    def reset_login_attemps(self):
        self.login_attemps = 0


class Admin(User):
    def __init__(self, first_name, last_name):
        super().__init__(first_name, last_name)
        self.privileges = Privileges()