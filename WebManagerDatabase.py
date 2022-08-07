#This file created the database and the table 
import mysql.connector

db=mysql.connector.connect(
    host="localhost",
    user="Lam",
    passwd="waterBell$73",
    database="appData"
)
#Created the database
#myCursor.execute("CREATE DATABASE appData")



#Create the table
#myCursor.execute("CREATE TABLE AppHistory (appName VARCHAR(50) PRIMARY KEY, clicks int DEFAULT 0, MostRecent boolean DEFAULT FALSE, NextRecent boolean DEFAULT FALSE)")

#Add all of the apps into the database
appNames=[("Outlook",),("Youtube",),("Google Calendar",),("Twitter",),("Google",),("Docs",),("Sheets",),("Linkedin",),("Canvas",),("Lionpath",),
("Bulletin",),("Chelsea",),("Typing",)]


#Insert the apps into the database with default values
'''
#q1="INSERT INTO AppHistory(appName) VALUES(%s)"
#myCursor.executemany(q1,appNames)
#db.commit()
'''




