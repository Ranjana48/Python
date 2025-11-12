import mysql.connector
cn = mysql.connector.connect(database="schools",
                     user = "root",
                     password = "ran0405",
                     host="localhost",
                     port=3306)
print("connection established")
print(cn)
cn.close()

