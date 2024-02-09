class Payment:
    def __init__(self,payment_id=0,payment_method=None,full_name=None,booking_id=0):
       #initialize
        self._payment_id=payment_id
        self._payment_method=payment_method
        self._full_name =full_name
        self._booking_id=booking_id

#getter/setter
    def get_payment_id(self):
        return self._payment_id

    def set_payment_id(self, payment_id):
        self._payment_id = payment_id

    def get_payment_method(self):
        return self._payment_method

    def set_payment_method(self, payment_method):
        self._payment_method = payment_method

    def get_full_name(self):
        return self._full_name

    def set_full_name(self, full_name):
        self._full_name = full_name

    def get_booking_id(self):
        return self._booking_id

    def set_booking_id(self, booking_id):
        self._booking_id = booking_id