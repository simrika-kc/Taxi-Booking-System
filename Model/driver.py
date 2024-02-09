class Driver:
    def __init__(self,driver_id=0,licence_plate=None,full_name=None,mobile=None,status=None,username=None,password=None,address=None):
        self._driver_id=driver_id
        self._licence_plate=licence_plate
        self._full_name =full_name
        self._mobile=mobile
        self._status = status
        self._username = username
        self._password = password
        self._address=address


#getter / setter
    def get_driver_id(self):
        return self._driver_id

    def set_driver_id(self, driver_id):
        self._driver_id = driver_id

    def get_licence_plate(self):
        return self._licence_plate

    def set_licence_plate(self, licence_plate):
        self._licence_plate = licence_plate

    def get_full_name(self):
        return self._full_name

    def set_full_name(self, full_name):
        self._full_name = full_name

    def get_mobile(self):
        return self._mobile

    def set_mobile(self, mobile):
        self._mobile = mobile

    def get_status(self):
        return self._status

    def set_status(self, status):
        self._status = status

    def get_username(self):
        return self._username

    def set_username(self, username):
        self._username = username

    def get_password(self):
        return self._password

    def set_password(self, password):
        self._password = password

    def get_address(self):
        return self._address

    def set_address(self, address):
        self._address = address
