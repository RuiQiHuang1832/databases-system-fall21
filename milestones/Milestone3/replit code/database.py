
# database.py
# Handles all the methods interacting with the database of the application.
# Students must implement their own methods here to meet the project requirements.

import os
import pymysql.cursors
import fetch as fe

mylist = []

db_host = os.environ['DB_HOST']
db_username = os.environ['DB_USER']
db_password = os.environ['DB_PASSWORD']
db_name = os.environ['DB_NAME']
myotherlist = []

conn = pymysql.connect(host=db_host,
                               port=3306,
                               user=db_username,
                               password=db_password,
                               db=db_name,
                               charset="utf8mb4", cursorclass=pymysql.cursors.DictCursor)
storage =[]
def connect():
    try:
        print("Bot connected to database {}".format(db_name))
        return conn
    except:
        print("Bot failed to create a connection with your database because your secret environment variables " +
              "(DB_HOST, DB_USER, DB_PASSWORD, DB_NAME) are not set".format(db_name))
        print("\n")
        
#Testing
mycursor = conn.cursor()

mycursor.execute("SELECT Donors.name FROM Patients JOIN Donors ON Patients.blood_type = Donors.blood_type WHERE Patients.name='Aatrox' OR Patients.name='Sammy'")

myresult = mycursor.fetchall()

for row in myresult:
  row = (row['name'])
  mylist.append(row)

mycursor.execute("SELECT Patients.name FROM Patients JOIN Donors ON Patients.blood_type = Donors.blood_type WHERE Patients.name='mari'")
myresult = mycursor.fetchall()

for x in myresult:
  x = (x['name'])
  myotherlist.append(x)   

def executemyorder(val):
    mycursor.execute("Select Donors.name FROM Donors JOIN Patients ON Donors.blood_type = Patients.blood_type Where amount > {}".format(val))
    myresult = mycursor.fetchall()
    storage.clear()
    for x in myresult:
      x = (x['name'])
      storage.append(x)


mycursor.execute("SELECT Reception.name FROM Reception JOIN BloodBank JOIN Exam ON Exam.idExam = BloodBank.inventory WHERE Reception.name='bob' OR Reception.name='cari'")
myresult = mycursor.fetchall()
receptions = []
for x in myresult:
  x = (x['name'])
  receptions.append(x)
del receptions[2:]      


listOfString = []
listofValues = []  
def findBloodtype(val):
    mycursor.execute("SELECT Patients.name FROM Patients JOIN Blood_type ON Blood_type.blood_type = Patients.blood_type WHERE Patients.blood_type = '{}'".format(val))
    myresult = mycursor.fetchall()
    listOfString.clear()
    for x in myresult:
        x = (x['name'])
        listOfString.append(x)
  
def rulefive(DOB, thetype):
  mycursor.execute("Select Patients.name FROM Patients JOIN Donors ON Donors.blood_type = Patients.blood_type WHERE Patients.DOB > '{}' AND Patients.blood_type = '{}'".format(DOB,thetype))
  myresult = mycursor.fetchall()  
  listofValues.clear()
  for x in myresult:
      x = (x['name'])
      listofValues.append(x)

rulesevenstring = []

def ruleseven(blood):
  mycursor.execute("Select Donors.name FROM Donors JOIN Patients ON Donors.blood_type = Patients.blood_type Where amount > {}".format(blood))
  myresult = mycursor.fetchall()
  rulesevenstring.clear()
  for x in myresult:
      x = (x['name'])
      rulesevenstring.append(x)

rulesixstring = []

def rulesix(val):
    mycursor.execute("SELECT Patients.name FROM Patients JOIN Blood_type ON Blood_type.blood_type = Patients.blood_type WHERE Patients.blood_type = '{}'".format(val))
    myresult = mycursor.fetchall()
    rulesixstring.clear()
    for x in myresult:
        x = (x['name'])
        rulesixstring.append(x)

