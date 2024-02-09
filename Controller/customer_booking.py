import sys

from Controller.database_connection import connection_control

#for booking

def booking_taxi(booking):
    conn = None
    result = False

    sql = "INSERT INTO booking(pickup_date,pickup_address,drop_off_address,status,customer_id) VALUES(%s,%s,%s,%s,%s)"
    values = (booking.get_pickup_date(), booking.get_pickup_address(), booking.get_dropoff_address(), booking.get_status(),booking.get_customer_id())
    try:
        conn = connection_control()
        cursor = conn.cursor()
        cursor.execute(sql, values)
        conn.close()
        cursor.close()
        result = True

    except:
        print("Error", sys.exc_info())

    finally:
        del values, sql, conn
        return result


#to get all the booking made by the customer in table

def for_table(booking):
    conn=None
    result=None
    sql="Select booking_id, pickup_address,Drop_off_address,pickup_date,status, driver_id from booking where customer_id=%s ORDER BY booking_id DESC"
    VALUES=(booking.get_customer_id(),)
    try:
        conn = connection_control()
        cursor = conn.cursor()
        cursor.execute(sql,VALUES)
        result=cursor.fetchall()
        conn.close()
        cursor.close()

    except:
        print("Error", sys.exc_info())

    finally:
        del VALUES, sql, conn
        return result


#for update
def update_booking(booking):
    conn=None
    result=False

    sql="UPDATE booking SET pickup_address=%s,Drop_off_address=%s, pickup_date=%s WHERE booking_id=%s AND status=%s "
    VALUE=(booking.get_pickup_address(),booking.get_dropoff_address(),booking.get_pickup_date(),booking.get_booking_id(),booking.get_status())

    try:
        conn=connection_control()
        cursor=conn.cursor()
        cursor.execute(sql,VALUE)

        cursor.close()
        conn.close()
        result=True

    except:
        print("error: ",sys.exc_info())

    finally:
        del sql,VALUE
        return result

#for cancel booking

def cancel_booking(booking):
    conn = None
    result = False

    sql = "DELETE FROM booking WHERE booking_id=%s AND status=%s "
    VALUE = (booking.get_booking_id(), booking.get_status())

    try:
        conn = connection_control()
        cursor = conn.cursor()
        cursor.execute(sql, VALUE)

        cursor.close()
        conn.close()
        result = True

    except:
        print("error: ", sys.exc_info())

    finally:
        del sql, VALUE
        return result






