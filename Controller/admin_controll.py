# Import necessary modules
import sys

# Import the connection_control function from the database_connection module in the Controller
from Controller.database_connection import connection_control

# Function to retrieve bookings with pending status
def showbookings():
    conn = None
    # SQL query to select specific booking details for pending bookings
    sql = """ SELECT booking_id, booking.customer_id, pickup_address, pickup_date, drop_off_address, status 
              FROM booking 
              INNER JOIN customer
              ON booking.customer_id = customer.customer_id
              WHERE status=%s 
              ORDER BY booking_id DESC"""
    VALUE = ("pending",)  # Value to be passed in the SQL query
    result = None

    try:
        conn = connection_control()  # Establish a database connection
        cursor = conn.cursor()  # Create a cursor object
        cursor.execute(sql, VALUE)  # Execute the SQL query with the provided value
        result = cursor.fetchall()  # Fetch all the results
        cursor.close()  # Close the cursor
        conn.close()  # Close the database connection

    except:
        print("Error: ", sys.exc_info())  # Handle any errors

    finally:
        del VALUE, sql, conn  # Clean up and free resources
        return result  # Return the result

# Function to assign a driver to a booking
def assign_driver(booking):
    conn = None
    result = False

    # SQL query to update the booking with the assigned driver and set the status
    sql = "UPDATE booking SET driver_id = %s , status = %s WHERE booking_id = %s"
    VALUE = (booking.get_driver_id(), booking.get_status(), booking.get_booking_id())

    # SQL query to update the driver status to "Reserved"
    sql1 = "UPDATE drivers SET status = %s WHERE driver_id = %s "
    value1 = ("Reserved", booking.get_driver_id())

    try:
        conn = connection_control()  # Establish a database connection
        cursor = conn.cursor()  # Create a cursor object
        cursor.execute(sql, VALUE)  # Execute the first SQL query
        cursor.execute(sql1, value1)  # Execute the second SQL query
        cursor.close()  # Close the cursor
        conn.close()  # Close the database connection
        result = True

    except:
        print("error: ", sys.exc_info())  # Handle any errors

    finally:
        del sql, VALUE  # Clean up and free resources
        return result  # Return the result

# Function to retrieve booking details
def booking_details():
    conn = None
    result = None
    # SQL query to select specific booking details for all bookings
    sql = """   SELECT booking_id, booking.customer_id, pickup_address, Drop_off_address, pickup_date, driver_id, status
                FROM booking
                JOIN customer ON booking.customer_id = customer.customer_id
                ORDER BY booking_id DESC;  """

    try:
        conn = connection_control()  # Establish a database connection
        cursor = conn.cursor()  # Create a cursor object
        cursor.execute(sql)  # Execute the SQL query
        result = cursor.fetchall()  # Fetch all the results
        cursor.close()  # Close the cursor
        conn.close()  # Close the database connection

    except:
        print("Error", sys.exc_info())  # Handle any errors

    finally:
        del sql, conn  # Clean up and free resources
        return result  # Return the result

# Function to retrieve customer information
def customer_table():
    conn = None
    # SQL query to select specific customer details
    sql = """ SELECT customer_id, full_name, address, phone_number, email, payment_method,user_name 
              FROM customer"""
    result = None

    try:
        conn = connection_control()  # Establish a database connection
        cursor = conn.cursor()  # Create a cursor object
        cursor.execute(sql)  # Execute the SQL query
        result = cursor.fetchall()  # Fetch all the results
        cursor.close()  # Close the cursor
        conn.close()  # Close the database connection

    except:
        print("Error: ", sys.exc_info())  # Handle any errors

    finally:
        del sql, conn  # Clean up and free resources
        return result  # Return the result
