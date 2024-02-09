import sys

from Controller.database_connection import connection_control

#for booking

def driver_register(driver):
    conn = None
    result = False

    sql = "INSERT IGNORE INTO drivers(licence_number,status,mobile,full_name,username,password,address) VALUES(%s,%s,%s,%s,%s,%s,%s)"
    values = (driver.get_licence_plate(), driver.get_status(), driver.get_mobile(), driver.get_full_name(),driver.get_username(),driver.get_password(),driver.get_address())
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


def fetchdriver_data():
    conn=None
    sql="SELECT driver_id,full_name,address,mobile,status FROM drivers ORDER BY driver_id DESC"

    result=None

    try:
        conn=connection_control()
        cursor=conn.cursor()
        cursor.execute(sql)

        result=cursor.fetchall()
        cursor.close()
        conn.close()


    except:
        print("Error: ",sys.exc_info())

    finally:
        del sql, conn
        return result
