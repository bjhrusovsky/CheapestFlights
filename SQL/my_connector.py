import mysql.connector
from Utils.OpenJProperties import openFile

configs = openFile("../SQL/app-config.properties")



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
