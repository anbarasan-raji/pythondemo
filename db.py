## Connecting to the database

## importing 'mysql.connector' as mysql for convenient
import mysql.connector as mysql
import json

## connecting to the database using 'connect()' method
## it takes 3 required parameters 'host', 'user', 'password', 'database'
conn = mysql.connect(
        host = "localhost",
        user = "root",
        password = "12345",
        database = "cposres_865211121_db"
    )

# mycursor = conn.cursor()

# mycursor.execute("show databases")

# for i in mycursor:
#     print(json.dumps(i))

# conn.close()