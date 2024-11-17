import pymysql

connection = pymysql.connect(
    host='localhost',
    user='ttms_admin',
    password='admin1@TTMS',
    database='ttms_db',
)
print("Connected successfully!")
connection.close()
