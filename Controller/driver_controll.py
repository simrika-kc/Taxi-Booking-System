import sys
from Controller.database_connection import connection_control
from Model import global_variable

def assigned_booking_details():
    conn = None
    result = None
    sql = """   SELECT booking_id, booking.customer_id, pickup_address, Drop_off_address, pickup_date, driver_id, status
                FROM booking
                JOIN customer ON booking.customer_id = customer.customer_id
                WHERE driver_id = %s
                ORDER BY booking_id DESC   """
    VALUE = (global_variable.driver[0],)
    try:
        conn = connection_control()
        cursor = conn.cursor()
        cursor.execute(sql,VALUE)
        result = cursor.fetchall()
        cursor.close()
        conn.close()

    except:
        print("Error", sys.exc_info())

    finally:
        del sql, conn
        return result

def fetchdriver_profile():
    conn=None
    sql="SELECT driver_id,full_name,address,mobile,status FROM drivers WHERE driver_id = %s ORDER BY driver_id DESC"
    values = (global_variable.driver[0],)
    result=None

    try:
        conn=connection_control()
        cursor=conn.cursor()
        cursor.execute(sql, values)

        result=cursor.fetchall()
        cursor.close()
        conn.close()


    except:
        print("Error: ",sys.exc_info())

    finally:
        del sql, conn
        return result

def complete_booking(booking):
    conn = None
    result = False

    sql = "UPDATE booking SET status = %s where booking_id = %s "
    VALUE = ("Completed", booking.get_booking_id())

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
