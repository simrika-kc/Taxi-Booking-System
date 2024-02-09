class Booking:
    def __init__(self,booking_id=0,pickup_date=None,pickup_address=None,dropoff_address=None,status=None,customer_id=0,driver_id=0,admin_id=0):
        # Initialize
        self._booking_id=booking_id
        self._pickup_date=pickup_date
        self._pickup_address =pickup_address
        self._dropoff_address=dropoff_address
        self._status = status
        self._customer_id = customer_id
        self._driver_id = driver_id
        self._admin_id=admin_id


#getter
    def get_booking_id(self):
        return self._booking_id

    def get_pickup_date(self):
        return self._pickup_date

    def get_pickup_address(self):
        return self._pickup_address

    def get_dropoff_address(self):
        return self._dropoff_address

    def get_status(self):
        return self._status

    def get_customer_id(self):
        return self._customer_id

    def get_driver_id(self):
        return self._driver_id

    def get_admin_id(self):
        return self._admin_id

     #setter
    def set_booking_id(self,booking_id):
        self._booking_id=booking_id

    def set_pickup_date(self,pickupdate):
        self._pickup_date=pickupdate

    def set_pickup_address(self, pickup_address):
        self._address = pickup_address

    def set_dropoff_address(self,dropoff_address):
        self._email=dropoff_address

    def set_status(self, status):
        self._status = status

    def set_customer_id(self, customer_id):
        self._customer_id = customer_id

    def set_driver_id(self,driver_id):
        self._driver_id=driver_id

    def set_admin_id(self,admin_id):
        self._admin_id=admin_id


