import mysql.connector

connection = mysql.connector.connect(
    #change names after creat a database
    host='localhost',
    user='client',
    password='client',
    database='school'
)