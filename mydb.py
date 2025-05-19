import mysql.connector

dataBase = mysql.connector.connect(
   host = 'localhost',
   user = 'root',
   passwd = 'mysql'
)

#prepare a cursor object
cursorObject = dataBase.cursor()


cursorObject.execute("CREATE DATABASE mycrm");

print("All Done!");