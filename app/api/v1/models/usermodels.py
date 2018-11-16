users = []


class Users(object):

    def __init__(self):
        self.db = users


def create_account(self, email, phone_number, user_name, password):
    account = {
        "user_id": str(len(users) + 1),
        "email": email,
        "phone_number": phone_number,
        "user_name": user_name,
        "password": password
    }

    self.db.append(account)
    return account


def get_users(self):
    res = self.db
    return res 


	





