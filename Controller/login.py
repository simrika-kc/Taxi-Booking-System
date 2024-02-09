import sys

from Controller.database_connection import connection_control


def  login_customer(customer):
    conn=None
    sql="SELECT * FROM customer WHERE user_name=%s AND password=%s"

    values=(customer.get_user_name(), customer.get_password())
    result=None

    try:
        conn=connection_control()
        cursor=conn.cursor()
        cursor.execute(sql,values)

        result=cursor.fetchone()
        cursor.close()
        conn.close()


    except:
        print("Error: ",sys.exc_info())

    finally:
        del values, sql, conn
        return result

def login_driver(driver):
    conn=None
    sql="SELECT * FROM drivers WHERE username=%s AND password=%s"

    values=(driver.get_username(), driver.get_password())
    result=None

    try:
        conn=connection_control()
        cursor=conn.cursor()
        cursor.execute(sql,values)

        result=cursor.fetchone()
        cursor.close()
        conn.close()


    except:
        print("Error: ",sys.exc_info())

    finally:
        del values, sql, conn
        return result

# for admin
def login_admin(admin):
    conn=None
    sql="SELECT * FROM admin WHERE username=%s AND password=%s"

    values=(admin.get_username(), admin.get_password())
    result=None

    try:
        conn=connection_control()
        cursor=conn.cursor()
        cursor.execute(sql,values)

        result=cursor.fetchone()
        cursor.close()
        conn.close()


    except:
        print("Error: ",sys.exc_info())

    finally:
        del values, sql, conn
        return result