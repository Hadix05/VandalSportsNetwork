import mysql.connector

cnx = mysql.connector.connect(user='root', password='',
                              host='127.0.0.1',
                              database='sports-db')

cursor = cnx.cursor()

query = ("SELECT * FROM Node")

cursor.execute(query)

for (name) in cursor:
  print("{}".format(name))

cursor.close()
cnx.close()