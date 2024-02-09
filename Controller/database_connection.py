import sys
import mysql.connector
def connection_control():
    conn=None 
    try:
        #connecting database
        conn=mysql.connector.connect(
            host="localhost",
            username="root",
            password="",
            database="taxibooking"
        )
    #    print("connected") #to check if the database is connected or not
    except:
        print("Error: ", sys.exc_info())

    finally:
        return conn

#connection_control() #to check if the database is connected or not
