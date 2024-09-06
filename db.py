import mysql.connector

connect = mysql.connector.connect(
    #change names after creat a database
    host='localhost',
    user='client',
    password='client',
    database='school'
)
