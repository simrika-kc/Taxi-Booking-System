class Admin:
    def __init__(self, admin_id=0, email=None, full_name=None, mobile=None, address=None, username=None, password=None):
       #initialize
        self._admin_id = admin_id
        self._email = email
        self._full_name = full_name
        self._mobile = mobile
        self._address = address
        self._username = username
        self._password = password

#getter and setter
    def get_admin_id(self):
        return self._admin_id

    def set_admin_id(self, admin_id):
        self._admin_id = admin_id

    def get_email(self):
        return self._email

    def set_email(self, email):
        self._email = email

    def get_full_name(self):
        return self._full_name

    def set_full_name(self, full_name):
        self._full_name = full_name

    def get_mobile(self):
        return self._mobile

    def set_mobile(self, mobile):
        self._mobile = mobile

    def get_address(self):
        return self._address

    def set_address(self, address):
        self._address = address

    def get_username(self):
        return self._username

    def set_username(self, username):
        self._username = username

    def get_password(self):
        return self._password

    def set_password(self, password):
        self._password = password
