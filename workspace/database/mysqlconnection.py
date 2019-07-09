import mysql.connector
from mysql.connector import Error

def connect():
    try:
        conn=mysql.connector.connect(host='192.168.1.81',database='pythondb',user='root',password='password')
        if conn.is_connected():
            print('Connected to MySQL database')          
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM employee")
            rows = cursor.fetchall()
            print('Total Row(s):', cursor.rowcount)
            for row in rows:
                print(row)
    except Error as e:
        print(e)
    finally:
        conn.close()

if __name__ == '__main__':
    connect()