import mysql.connector


def connect_to_db():
    cnx = mysql.connector.connect(
        host="127.0.0.1",
        database="sports-db",
        user="root",
        password=""
    )
    return cnx
