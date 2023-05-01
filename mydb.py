import mysql.connector

database = mysql.connector.connect(
    host='localhost',
    user='root',
    passwd='M@sterpiece1'
)

cursorObject=database.cursor()
cursorObject.execute(
    "CREATE DATABASE power"
)
print("All DDNDND")