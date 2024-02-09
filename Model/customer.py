class Customer:
    def __init__(self,customer_id=0,full_name=None,address=None,email=None,phone_number=None,payment_method=None,user_name=None,password=None):
        #initialize
        self._customer_id=customer_id
        self._full_name=full_name
        self._address=address
        self._email=email
        self._phone_number=phone_number
        self._payment_method=payment_method
        self._user_name=user_name
        self._password=password

#getter
    def get_customer_id(self):
        return self._customer_id

    def get_full_name(self):
        return self._full_name

    def get_address(self):
        return self._address

    def get_email(self):
        return self._email

    def get_phone_number(self):
        return self._phone_number

    def get_payment_method(self):
        return self._payment_method

    def get_user_name(self):
        return self._user_name

    def get_password(self):
        return self._password

     #setter
    def set_customer_id(self,customer_id):
        self._customer_id=customer_id

    def set_full_name(self,full_name):
        self._full_name=full_name

    def set_address(self, address):
        self._address = address

    def set_email(self,email):
        self._email=email

    def set_phone_number(self, phone_number):
        self._phone_number = phone_number

    def set_payment_method(self, payment_method):
        self._payment_method = payment_method

    def set_user_name(self,user_name):
        self._user_name=user_name

    def set_password(self,password):
        self._password=password


