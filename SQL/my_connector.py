import mysql.connector
from jproperties import Properties

configs = Properties()
#Grab our DB information securely.
with open('app-config.properties', 'rb') as config_file:
    configs.load(config_file)



#First thing, let's connect to our database.
mydb = mysql.connector.connect(
    host=configs.get("host").data,
    user=configs.get("user").data,
    password=configs.get("password").data,
    port=configs.get("port").data,
    database=configs.get("database").data
)

#This cursor allows us to run queries.
mycursor = mydb.cursor()


#MAKE SURE WE DELETE AT THE END ******************************************************
# mycursor.execute('SELECT * FROM Websites;')
#
# users = mycursor.fetchall()
#
# for user in users:
#     print(user)
