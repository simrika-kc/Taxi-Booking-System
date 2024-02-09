import sys

from Controller.database_connection import connection_control

#for login


#for registration
def register_customer(customer):
        conn=None
        result=False

        sql="INSERT INTO customer(full_name,address,email,phone_number,payment_method,user_name,password) VALUES(%s,%s,%s,%s,%s,%s,%s)"
        values=(customer.get_full_name(),customer.get_address(),customer.get_email(),customer.get_phone_number(),customer.get_payment_method(),customer.get_user_name(),customer.get_password())
        try:
            conn=connection_control()
            cursor=conn.cursor()
            cursor.execute(sql,values)
            conn.close()
            cursor.close()
            result=True

        except:
            print("Error", sys.exc_info())

        finally:
            del values,sql,conn
            return result


