#Created By: James Kyle Harrison
#Requires mysql-connector-python and tabulate
import datetime
import mysql.connector
from tkinter import *
from tkinter.ttk import Combobox
import array as arr
from tabulate import tabulate

cnx = mysql.connector.connect(user='root',password='password',host='127.0.0.1', database='testschema')
cursor = cnx.cursor()
queries = []

"""
Initial Querying
"""
def createQuery(): #Used in obtaining Data for OLAP to SQL Query Conversion
  cnx2 = mysql.connector.connect(user='root',password='password',host='127.0.0.1', database='testschema')
  cursor2 = cnx2.cursor()
  #selectQuery = ["SELECT s.AcademicID, s.CollegeID, s.SemesterID"]
  selectQuery = ["SELECT"]
  fromQuery = ["FROM students s"]
  whereQuery = ["WHERE"]
  gpaInput = input1.get("1.0", "end-1c")
  statusInput = input2.get("1.0", "end-1c")
  nameInput = input3.get("1.0", "end-1c")
  addressInput = input4.get("1.0", "end-1c")
  gpabox1Input = gpaBox1.get()
  gpabox2Input = gpaBox2.get()
  gpabox3Input = gpaBox3.get()
  collegebox1Input = collegeBox1.get()
  collegebox2Input = collegeBox2.get()
  collegebox3Input = collegeBox3.get()
  collegebox4Input = collegeBox4.get()
  majorInput = input5.get("1.0", "end-1c")
  degreeInput = input6.get("1.0", "end-1c")
  yearInput = input7.get("1.0", "end-1c")
  #monthInput = input8.get("1.0", "end-1c")
  month1Input = semesterBox1.get()
  month2Input = semesterBox2.get()
  month3Input = semesterBox3.get()
  month4Input = semesterBox4.get()
  month5Input = semesterBox5.get()
  month6Input = semesterBox6.get()
  operation = cb.get()

  splitter = []
  message = "("
  #Creates individual statements representing the query segments.
  if(gpaInput != "" or statusInput != "" or nameInput != "" or addressInput != "" or gpabox1Input != "" or gpabox2Input != "" or gpabox3Input != ""):
    fromQuery.append("academics a")
    whereQuery.append("a.AcademicID = s.AcademicID")
    if(gpaInput != ""):
      selectQuery.append("a.GPA")
      if("Slice" in operation or "Dice" in operation):
        if(" OR " in gpaInput): #If there are multiple inputs
          splitter = gpaInput.split(" OR ")
          for x in splitter:
            if(x == splitter[len(splitter)-1]):
              message += "a.GPA = " + x +")"
            else:  
              message += "a.GPA = " + x + " OR "
          whereQuery.append(message)
          splitter = []
          message = "("   
        else:
          whereQuery.append("a.GPA = " + gpaInput)
    if(statusInput != ""):
      selectQuery.append("a.Status")
      if("Slice" in operation or "Dice" in operation):
        if(" OR " in statusInput): #If there are multiple inputs
          splitter = statusInput.split(" OR ")
          for x in splitter:
            if(x == splitter[len(splitter)-1]):
              message += "a.Status = '" + x +"')"
            else:  
              message += "a.Status = '" + x + "' OR "
          whereQuery.append(message)
          splitter = []
          message = "("   
        else:
          whereQuery.append("a.Status = '" + statusInput + "'")
    if(addressInput != ""):
      selectQuery.append("a.Address")
      if("Slice" in operation or "Dice" in operation):
        if(" OR " in addressInput): #If there are multiple inputs
          splitter = addressInput.split(" OR ")
          for x in splitter:
            if(x == splitter[len(splitter)-1]):
              message += "a.Address = '" + x +"')"
            else:  
              message += "a.Address = '" + x + "' OR "
          whereQuery.append(message)
          splitter = []
          message = "("   
        else:
          whereQuery.append("a.Address = '" + addressInput + "'")
    if(nameInput != ""):
      selectQuery.append("a.Name")
      if("Slice" in operation or "Dice" in operation):
        if(" OR " in nameInput): #If there are multiple inputs
          splitter = nameInput.split(" OR ")
          for x in splitter:
            if(x == splitter[len(splitter)-1]):
              message += "a.Name = '" + x +"')"
            else:  
              message += "a.Name = '" + x + "' OR "
          whereQuery.append(message)
          splitter = []
          message = "("   
        else:
          whereQuery.append("a.Name = '" + nameInput + "'")

    message = ""
    if(gpabox1Input == "1"):
      if("a.gpaQuality" not in selectQuery):
        selectQuery.append("a.gpaQuality")
      if("Slice" in operation or "Dice" in operation):
        if(gpabox2Input == "1" or gpabox3Input == "1"):
          message += "(a.gpaQuality = 'high' OR "
        else:
          whereQuery.append("a.gpaQuality = 'high'")
    if(gpabox2Input == "1"):
      if("a.gpaQuality" not in selectQuery):
        selectQuery.append("a.gpaQuality")
      if("Slice" in operation or "Dice" in operation):
        if(gpabox1Input != "1" and gpabox3Input == "1"):
          message += "(a.gpaQuality = 'medium' OR "
        elif(gpabox1Input == "1" and gpabox3Input == "1"):
          message += "a.gpaQuality = 'medium' OR "
        elif(gpabox1Input == "1" and gpabox3Input != "1"):
          message += "a.gpaQuality = 'medium')"
          whereQuery.append(message)
        else:  
          whereQuery.append("a.gpaQuality = 'medium'")
    if(gpabox3Input == "1"):
      if("a.gpaQuality" not in selectQuery):
        selectQuery.append("a.gpaQuality")
      if("Slice" in operation or "Dice" in operation):
        if(gpabox1Input == "1" or gpabox2Input == "1"):
          message += "a.gpaQuality = 'low')"
          whereQuery.append(message)
        else:
          whereQuery.append("a.gpaQuality = 'low'")


  if(collegebox1Input != "" or collegebox2Input != "" or collegebox3Input != "" or collegebox4Input != "" or majorInput != "" or degreeInput != ""):
    fromQuery.append("program p")
    whereQuery.append("p.CollegeID = s.CollegeID")
    if(collegebox1Input == "1"):
      if("p.College" not in selectQuery):
        selectQuery.append("p.College")
      if("Slice" in operation or "Dice" in operation):
        whereQuery.append("p.College = 'Cyber College'")
    if(collegebox2Input == "1"):
      if("p.College" not in selectQuery):
        selectQuery.append("p.College")
      if("Slice" in operation or "Dice" in operation):
        whereQuery.append("p.College = 'College of Business'")
    if(collegebox3Input == "1"):
      if("p.College" not in selectQuery):
        selectQuery.append("p.College")
      if("Slice" in operation or "Dice" in operation):
        whereQuery.append("p.College = 'College of Education'")
    if(collegebox4Input == "1"):
      if("p.College" not in selectQuery):
        selectQuery.append("p.College")
      if("Slice" in operation or "Dice" in operation):
        whereQuery.append("p.College = 'College of Art of Science'")
    if(majorInput != ""):
      selectQuery.append("p.Major")
      if("Slice" in operation or "Dice" in operation):
        whereQuery.append("p.Major = '" + majorInput + "'")
    if(degreeInput != ""):
      selectQuery.append("p.Degree")
      if("Slice" in operation or "Dice" in operation):
        whereQuery.append("p.Degree = '" + degreeInput + "'")  


  if(yearInput != "" or month1Input != "" or month2Input != "" or month3Input != "" or month4Input != "" or month5Input != "" or month6Input != ""):
    fromQuery.append("time t")
    whereQuery.append("t.SemesterID = s.SemesterID")
    if(yearInput != ""): 
      selectQuery.append("t.Y")
      if("Slice" in operation or "Dice" in operation):
        if(" OR " in yearInput): #If there are multiple inputs
          splitter = yearInput.split(" OR ")
          for x in splitter:
            if(x == splitter[len(splitter)-1]):
              message += "t.Y = " + x +")"
            elif(x == splitter[0]):
              message += "(t.Y = " + x + " OR "
            else:  
              message += "t.Y = " + x + " OR "
          whereQuery.append(message)
          splitter = []
          message = "("   
        else: #If there is one input 
          whereQuery.append("t.Y = " + yearInput + "")
    if(month1Input == "1" or month2Input == "1" or month3Input == "1" or month4Input == "1" or month5Input == "1" or month6Input == "1"):
      selectQuery.append("t.MonthDay")
      if("Slice" in operation or "Dice" in operation):
        message = ""
        if(month1Input == "1"):
          if(month2Input != "1" and month3Input != "1" and month4Input != "1" and month5Input != "1" and month6Input != "1"):
            message += "t.MonthDay = 'May-15'"
          else:
            message += "(t.MonthDay = 'May-15' OR "
        if(month2Input == "1"):
          if(month1Input != "1" and month3Input != "1" and month4Input != "1" and month5Input != "1" and month6Input != "1"):
            message += "t.MonthDay = 'Jun-1'"
          elif(month1Input != "1" and (month3Input == "1" or month4Input == "1" or month5Input == "1" or month6Input == "1")):
            message += "(t.MonthDay = 'Jun-1' OR "
          elif(month1Input == "1" and (month3Input == "1" or month4Input == "1" or month5Input == "1" or month6Input == "1")):
            message += "t.MonthDay = 'Jun-1' OR "
          else:
            message += "t.MonthDay = 'Jun-1')"
        if(month3Input == "1"):
          if(month1Input != "1" and month2Input != "1" and month4Input != "1" and month5Input != "1" and month6Input != "1"):
            message += "t.MonthDay = 'Jul-4'"
          elif(month1Input != "1" and month2Input != "1" and (month4Input == "1" or month5Input == "1" or month6Input == "1")):
            message += "(t.MonthDay = 'Jul-4' OR "
          elif((month2Input == "1" or month1Input == "1") and (month4Input == "1" or month5Input == "1" or month6Input == "1")):
            message += "t.MonthDay = 'Jul-4' OR "
          else:
            message += "t.MonthDay = 'Jul-4')"
        if(month4Input == "1"):
          if(month1Input != "1" and month2Input != "1" and month3Input != "1" and month5Input != "1" and month6Input != "1"):
            message += "t.MonthDay = 'Jul-15'"
          elif(month1Input != "1" and month2Input != "1" and month3Input == "1" and (month5Input == "1" or month6Input == "1")):
            message += "(t.MonthDay = 'Jul-15' OR "
          elif((month2Input == "1" or month1Input == "1" or month3Input == "1") and (month5Input == "1" or month6Input == "1")):
            message += "t.MonthDay = 'Jul-15' OR "
          else:
            message += "t.MonthDay = 'Jul-15')"
        if(month5Input == "1"):
          if(month1Input != "1" and month2Input != "1" and month4Input != "1" and month3Input != "1" and month6Input != "1"):
            message += "t.MonthDay = 'Aug-15'"
          elif(month1Input != "1" and month2Input != "1" and month3Input != "1" and month4Input != "1" and (month6Input == "1")):
            message += "(t.MonthDay = 'Aug-15' OR "
          elif((month2Input == "1" or month1Input == "1" or month3Input == "1" or month4Input == "1") and (month6Input == "1")):
            message += "t.MonthDay = 'Aug-15' OR "
          else:
            message += "t.MonthDay = 'Aug-15')"
        if(month6Input == "1"):
          if(month1Input != "1" and month2Input != "1" and month3Input != "1" and month4Input != "1" and month5Input != "1"):
            message += "t.MonthDay = 'Dec-15'"
          else:
            message += "t.MonthDay = 'Dec-15')"
        whereQuery.append(message)
        


#Puts the query statement pieces together to finally use in connection to MySQL
  finalQuery = ""
  for x in selectQuery:
    if(x == selectQuery[0] or x == selectQuery[1]):
      finalQuery += x + " "
    elif(x == selectQuery[len(selectQuery)-1]):
      finalQuery += ", " + x + " "
    else:
      finalQuery += ", " + x  
  for x in fromQuery:
    if(x == fromQuery[0]):
      finalQuery += x + ""
    elif(x == fromQuery[len(fromQuery)-1]):
      finalQuery += ", " + x + " "
    else:
      finalQuery += ", " + x
  for x in whereQuery:
    if(x == whereQuery[0]):
      finalQuery += x
    elif (x == whereQuery[1]):
      finalQuery += " " + x
    else:
      finalQuery += " AND " + x
  print(finalQuery)

  cursor2.execute(finalQuery)
  result = cursor2.fetchall()

  #This block prints out the query results
  #heads = ['AcademicID', 'CollegeID', 'SemesterID']
  heads = []
  splits = ""
  for x in selectQuery:
    if(x == selectQuery[0]):
      splits = ""
    else:
      splits = x
      splits = splits.split('.', 1)
      heads.append(splits[1])
  print(tabulate(result, headers=heads, tablefmt='psql'))
  print("Returning " + str(len(result)) + " resulting Students in this query.")
  queries.append(finalQuery)

"""
Continue Querying Created Cube
"""

def continueQuery():
  operation = cb.get()
  if("Rollup" in operation or "Rolldown" in operation):
    olapRoll()
  elif("Slice" in operation):
    olapSlice()
  elif("Dice" in operation):
    olapDice()
  elif("Pivot" in operation):
    olapPivot()

def olapRoll(): #Replace the attributes in the SELECT Statement to represent changing tiers in the hierarchy
  statement = queries[len(queries)-1].split("FROM")
  selectQuery = statement[0].split(",")
  #print(selectQuery)

  cnx2 = mysql.connector.connect(user='root',password='password',host='127.0.0.1', database='testschema')
  cursor2 = cnx2.cursor()
  gpaInput = input1.get("1.0", "end-1c")
  statusInput = input2.get("1.0", "end-1c")
  nameInput = input3.get("1.0", "end-1c")
  addressInput = input4.get("1.0", "end-1c")
  gpabox1Input = gpaBox1.get()
  gpabox2Input = gpaBox2.get()
  gpabox3Input = gpaBox3.get()
  collegebox1Input = collegeBox1.get()
  collegebox2Input = collegeBox2.get()
  collegebox3Input = collegeBox3.get()
  collegebox4Input = collegeBox4.get()
  majorInput = input5.get("1.0", "end-1c")
  degreeInput = input6.get("1.0", "end-1c")
  yearInput = input7.get("1.0", "end-1c")
  #monthInput = input8.get("1.0", "end-1c")
  month1Input = semesterBox1.get()
  month2Input = semesterBox2.get()
  month3Input = semesterBox3.get()
  month4Input = semesterBox4.get()
  month5Input = semesterBox5.get()
  month6Input = semesterBox6.get()

  if(gpaInput != "" or statusInput != "" or nameInput != "" or addressInput != "" or gpabox1Input != "" or gpabox2Input != "" or gpabox3Input != ""):
    for x in selectQuery:
      if "a." in x:
        selectQuery.remove(x)
    if(gpaInput != ""):
      selectQuery.append("a.GPA")
    if(statusInput != ""):
      selectQuery.append("a.Status")
    if(addressInput != ""):
      selectQuery.append("a.Address")
    if(nameInput != ""):
      selectQuery.append("a.Name")
    if(gpabox1Input == "1"):
      if("a.gpaQuality" not in selectQuery):
        selectQuery.append("a.gpaQuality")
    if(gpabox2Input == "1"):
      if("a.gpaQuality" not in selectQuery):
        selectQuery.append("a.gpaQuality")
    if(gpabox3Input == "1"):
      if("a.gpaQuality" not in selectQuery):
        selectQuery.append("a.gpaQuality")

  if(collegebox1Input != "" or collegebox2Input != "" or collegebox3Input != "" or collegebox4Input != "" or majorInput != "" or degreeInput != ""):
    for x in selectQuery:      
      if "p." in x:
        selectQuery.remove(x)
    if(collegebox1Input == "1"):
      if("p.College" not in selectQuery):
        selectQuery.append("p.College")
    if(collegebox2Input == "1"):
      if("p.College" not in selectQuery):
        selectQuery.append("p.College")  
    if(collegebox3Input == "1"):
      if("p.College" not in selectQuery):
        selectQuery.append("p.College")  
    if(collegebox4Input == "1"):
      if("p.College" not in selectQuery):
        selectQuery.append("p.College")
    if(majorInput != ""):
      selectQuery.append("p.Major")
    if(degreeInput != ""):
      selectQuery.append("p.Degree")
    
  if(yearInput != "" or month1Input != "" or month2Input != "" or month3Input != "" or month4Input != "" or month5Input != "" or month6Input != ""):
    for x in selectQuery:
      if "t." in x:
        selectQuery.remove(x)
    if(yearInput != ""): 
      selectQuery.append("t.Y")
    if(month1Input == "1" or month2Input == "1" or month3Input == "1" or month4Input == "1" or month5Input == "1" or month6Input == "1"):
      selectQuery.append("t.MonthDay")
  print(selectQuery)      

  finalQuery = ""
  if "SELECT" not in selectQuery[0]:
    finalQuery = "SELECT "
  for x in selectQuery:
    if(x == selectQuery[0]):
      finalQuery += x + ""
    elif(x == selectQuery[len(selectQuery)-1]):
      finalQuery += ", " + x + " "
    else:
      finalQuery += ", " + x
  finalQuery += "FROM " + statement[1] 
  print(finalQuery)

  cursor2.execute(finalQuery)
  result = cursor2.fetchall()

  #This block prints out the query results
  #heads = ['AcademicID', 'CollegeID', 'SemesterID']
  heads = []
  splits = ""
  for x in selectQuery:
    #if(x == selectQuery[0] or x == selectQuery[1] or x == selectQuery[2]):
      #splits = ""
    #else:
    splits = x
    splits = splits.split('.', 1)
    heads.append(splits[1])
  print(tabulate(result, headers=heads, tablefmt='psql'))
  print("Returning " + str(len(result)) + " resulting Students in this query.")
  queries.append(finalQuery)                               

def olapSlice(): #Removes a attributes such that we are querying
  statement = queries[len(queries)-1].split("WHERE")
  whereQuery = statement[1].split(" AND ")

  cnx2 = mysql.connector.connect(user='root',password='password',host='127.0.0.1', database='testschema')
  cursor2 = cnx2.cursor()
  gpaInput = input1.get("1.0", "end-1c")
  statusInput = input2.get("1.0", "end-1c")
  nameInput = input3.get("1.0", "end-1c")
  addressInput = input4.get("1.0", "end-1c")
  gpabox1Input = gpaBox1.get()
  gpabox2Input = gpaBox2.get()
  gpabox3Input = gpaBox3.get()
  collegebox1Input = collegeBox1.get()
  collegebox2Input = collegeBox2.get()
  collegebox3Input = collegeBox3.get()
  collegebox4Input = collegeBox4.get()
  majorInput = input5.get("1.0", "end-1c")
  degreeInput = input6.get("1.0", "end-1c")
  yearInput = input7.get("1.0", "end-1c")
  #monthInput = input8.get("1.0", "end-1c")
  month1Input = semesterBox1.get()
  month2Input = semesterBox2.get()
  month3Input = semesterBox3.get()
  month4Input = semesterBox4.get()
  month5Input = semesterBox5.get()
  month6Input = semesterBox6.get()

  message = ""
  sliceInput = ""
  if(gpaInput != ""):
    message = "a.GPA"
    sliceInput = gpaInput
  elif(statusInput != ""):
    message = "a.Status"
    sliceInput = statusInput
  elif(addressInput != ""):
    message = "a.Address"
    sliceInput = addressInput
  elif(nameInput != ""):
    message = "a.Name"
    sliceInput = nameInput
  elif(gpabox1Input == "1" or gpabox2Input == "1" or gpabox3Input == "1"):
    message = "a.gpaQuality"
    if(gpabox1Input == "1"):
      sliceInput = "high"
    elif(gpabox2Input == "1"):
      sliceInput = "medium"
    elif(gpabox3Input == "1"):
      sliceInput = "low"
  elif(collegebox1Input == "1" or collegebox2Input == "1" or collegebox3Input == "1" or collegebox4Input == "1"):
    message = "p.College"
    if(collegebox1Input == "1"):
      sliceInput = "Cyber College"
    if(collegebox2Input == "1"):
      sliceInput = "College of Business"
    if(collegebox3Input == "1"):
      sliceInput = "College of Education"
    if(collegebox4Input == "1"):
      sliceInput = "College of Art of Science"
  elif(majorInput != ""):
    message = "p.Major"
    sliceInput = majorInput
  elif(degreeInput != ""):
    message = "p.Degree"
    sliceInput = degreeInput
  elif(yearInput != ""):
    message = "t.Y"
    sliceInput = yearInput
  elif(month1Input != "" or month2Input != "" or month3Input != "" or month4Input != "" or month5Input != "" or month6Input != ""):
    message = "t.MonthDay"
    if(month1Input == "1"):
      sliceInput = "May-15"
    if(month2Input == "1"):
      sliceInput = "Jun-1"
    if(month3Input == "1"):
      sliceInput = "Jul-4"
    if(month4Input == "1"):
      sliceInput = "Jul-15"
    if(month5Input == "1"):
      sliceInput = "Aug-15"
    if(month6Input == "1"):
      sliceInput = "Dec-15"
  
  for x in whereQuery:
    if message in x and "p.CollegeID" not in x:
      whereQuery.remove(x)
  
  finalQuery = statement[0] + " WHERE "
  for x in whereQuery:
    if(x == whereQuery[0]):
      finalQuery += x
    else:
      finalQuery += " AND " + x
  if(sliceInput != "1"):
    finalQuery += " AND " + message + " = '" + sliceInput + "'"
  print(finalQuery)
  cursor2.execute(finalQuery)
  result = cursor2.fetchall()

  #This block prints out the query results
  select = statement[0].split("FROM")
  selectQuery = select[0].split(',')
  #heads = ['AcademicID', 'CollegeID', 'SemesterID']
  heads = []
  splits = ""
  for x in selectQuery:
    #if(x == selectQuery[0] or x == selectQuery[1] or x == selectQuery[2]):
      #splits = ""
    #else:
    splits = x
    splits = splits.split('.', 1)
    heads.append(splits[1])
  print(tabulate(result, headers=heads, tablefmt='psql'))
  print("Returning " + str(len(result)) + " resulting Students in this query.")
  queries.append(finalQuery)                               



def olapDice(): #Replace the attributes in the WHERE Clause to represent a dicing of the cube
  statement = queries[len(queries)-1].split("WHERE")
  whereQuery = statement[1].split(",")
  orderBy = ""
  if " ORDER BY " in whereQuery:
    orderBy = whereQuery.split("ORDER BY")

  cnx2 = mysql.connector.connect(user='root',password='password',host='127.0.0.1', database='testschema')
  cursor2 = cnx2.cursor()
  gpaInput = input1.get("1.0", "end-1c")
  statusInput = input2.get("1.0", "end-1c")
  nameInput = input3.get("1.0", "end-1c")
  addressInput = input4.get("1.0", "end-1c")
  gpabox1Input = gpaBox1.get()
  gpabox2Input = gpaBox2.get()
  gpabox3Input = gpaBox3.get()
  collegebox1Input = collegeBox1.get()
  collegebox2Input = collegeBox2.get()
  collegebox3Input = collegeBox3.get()
  collegebox4Input = collegeBox4.get()
  majorInput = input5.get("1.0", "end-1c")
  degreeInput = input6.get("1.0", "end-1c")
  yearInput = input7.get("1.0", "end-1c")
  #monthInput = input8.get("1.0", "end-1c")
  month1Input = semesterBox1.get()
  month2Input = semesterBox2.get()
  month3Input = semesterBox3.get()
  month4Input = semesterBox4.get()
  month5Input = semesterBox5.get()
  month6Input = semesterBox6.get()

  if(gpaInput != "" or statusInput != "" or nameInput != "" or addressInput != "" or gpabox1Input != "" or gpabox2Input != "" or gpabox3Input != ""):
    if(gpaInput != ""):
      if(" OR " in gpaInput): #If there are multiple inputs
        splitter = gpaInput.split(" OR ")
        for x in splitter:
          if(x == splitter[len(splitter)-1]):
            message += "a.GPA = " + x +")"
          else:  
            message += "a.GPA = " + x + " OR "
        whereQuery.append(message)
        splitter = []
        message = "("   
      else:
        whereQuery.append("a.GPA = " + gpaInput)
    if(statusInput != ""):
      if(" OR " in statusInput): #If there are multiple inputs
        splitter = statusInput.split(" OR ")
        for x in splitter:
          if(x == splitter[len(splitter)-1]):
            message += "a.Status = '" + x +"')"
          else:  
            message += "a.Status = '" + x + "' OR "
        whereQuery.append(message)
        splitter = []
        message = "("   
      else:
        whereQuery.append("a.Status = '" + statusInput + "'")
    if(addressInput != ""):
      if(" OR " in addressInput): #If there are multiple inputs
        splitter = addressInput.split(" OR ")
        for x in splitter:
          if(x == splitter[len(splitter)-1]):
            message += "a.Address = '" + x +"')"
          else:  
            message += "a.Address = '" + x + "' OR "
        whereQuery.append(message)
        splitter = []
        message = "("   
      else:
        whereQuery.append("a.Address = '" + addressInput + "'")
    if(nameInput != ""):
      if(" OR " in nameInput): #If there are multiple inputs
        splitter = nameInput.split(" OR ")
        for x in splitter:
          if(x == splitter[len(splitter)-1]):
            message += "a.Name = '" + x +"')"
          else:  
            message += "a.Name = '" + x + "' OR "
        whereQuery.append(message)
        splitter = []
        message = "("   
      else:
        whereQuery.append("a.Name = '" + nameInput + "'")
    message = ""
    if(gpabox1Input == "1"):
      if(gpabox2Input == "1" or gpabox3Input == "1"):
        message += "(a.gpaQuality = 'high' OR "
      else:
        whereQuery.append("a.gpaQuality = 'high'")
    if(gpabox2Input == "1"):
      if(gpabox1Input != "1" and gpabox3Input == "1"):
        message += "(a.gpaQuality = 'medium' OR "
      elif(gpabox1Input == "1" and gpabox3Input == "1"):
        message += "a.gpaQuality = 'medium' OR "
      elif(gpabox1Input == "1" and gpabox3Input != "1"):
        message += "a.gpaQuality = 'medium')"
        whereQuery.append(message)
      else:  
        whereQuery.append("a.gpaQuality = 'medium'")
    if(gpabox3Input == "1"):
      if(gpabox1Input == "1" or gpabox2Input == "1"):
        message += "a.gpaQuality = 'low')"
        whereQuery.append(message)
      else:
        whereQuery.append("a.gpaQuality = 'low'")
      
  if(collegebox1Input != "" or collegebox2Input != "" or collegebox3Input != "" or collegebox4Input != "" or majorInput != "" or degreeInput != ""):
    message = ""
    if(collegebox1Input == "1"):
      if(collegebox2Input == "1" or collegebox3Input == "1" or collegebox4Input == "1"):
        message += "(p.College = 'Cyber College' OR "
      else:  
        message += "p.College = 'Cyber College'"
    if(collegebox2Input == "1"):
      if(collegebox1Input == "0" and (collegebox3Input == "1" or collegebox4Input == "1")):
        message += "(p.College = 'College of Business' OR "
      elif(collegebox1Input == "1" and (collegebox3Input == "1" or collegebox4Input == "1")):
        message += "p.College = 'College of Business' OR "
      elif(collegebox1Input == "1" and collegebox3Input == "0" and collegebox4Input == "0"):
        message += "p.College = 'College of Business')"
      else:
       message += "p.College = 'College of Business'"
    if(collegebox3Input == "1"):
      if((collegebox1Input == "1" or collegebox2Input == "1") and collegebox4Input == "1"):
        message += "p.College = 'College of Education' OR "
      elif((collegebox1Input == "1" or collegebox2Input == "1") and collegebox4Input == "0"):
        message += "p.College = 'College of Education')"
      elif((collegebox1Input == "0" or collegebox2Input == "0") and collegebox4Input == "1"):
        message += "(p.College = 'College of Education' OR"
      else:
        message +="p.College = 'College of Education'"
    if(collegebox4Input == "1"):
      if(collegebox1Input == "1" or collegebox2Input == "1" or collegebox3Input == "1"):
        message+="p.College = 'College of Art and Science')"
      else:
        message += "p.College = 'College of Art and Science'"
    whereQuery.append(message)
    message = "("
    if(majorInput != ""):
      if(" OR " in majorInput): #If there are multiple inputs
        splitter = majorInput.split(" OR ")
        for x in splitter:
          if(x == splitter[len(splitter)-1]):
            message += "p.Major = '" + x +"')"
          else:  
            message += "p.Major = '" + x + "' OR "
        whereQuery.append(message)
        splitter = []
        message = "("   
      else:
        whereQuery.append("p.Major = '" + majorInput + "'")
    if(degreeInput != ""):
      if(" OR " in degreeInput): #If there are multiple inputs
        splitter = degreeInput.split(" OR ")
        for x in splitter:
          if(x == splitter[len(splitter)-1]):
            message += "p.Degree = '" + x +"')"
          else:  
            message += "p.Degree = '" + x + "' OR "
        whereQuery.append(message)
        splitter = []
        message = "("   
      else:
        whereQuery.append("p.Degree = '" + degreeInput + "'")
      
    
  if(yearInput != "" or month1Input != "" or month2Input != "" or month3Input != "" or month4Input != "" or month5Input != "" or month6Input != ""):
    message = ""
    if(yearInput != ""): 
      if(" OR " in yearInput): #If there are multiple inputs
        splitter = yearInput.split(" OR ")
        for x in splitter:
          if(x == splitter[len(splitter)-1]):
            message += "t.Y = " + x +")"
          elif(x == splitter[0]):
            message += "(t.Y = " + x + " OR "
          else:  
            message += "t.Y = " + x + " OR "
        whereQuery.append(message)
        splitter = []
        message = "("   
      else: #If there is one input 
        whereQuery.append("t.Y = " + yearInput + "")
    if(month1Input == "1" or month2Input == "1" or month3Input == "1" or month4Input == "1" or month5Input == "1" or month6Input == "1"):
      message = ""
      if(month1Input == "1"):
        if(month2Input != "1" and month3Input != "1" and month4Input != "1" and month5Input != "1" and month6Input != "1"):
          message += "t.MonthDay = 'May-15'"
        else:
          message += "(t.MonthDay = 'May-15' OR "
      if(month2Input == "1"):
        if(month1Input != "1" and month3Input != "1" and month4Input != "1" and month5Input != "1" and month6Input != "1"):
          message += "t.MonthDay = 'Jun-1'"
        elif(month1Input != "1" and (month3Input == "1" or month4Input == "1" or month5Input == "1" or month6Input == "1")):
          message += "(t.MonthDay = 'Jun-1' OR "
        elif(month1Input == "1" and (month3Input == "1" or month4Input == "1" or month5Input == "1" or month6Input == "1")):
          message += "t.MonthDay = 'Jun-1' OR "
        else:
          message += "t.MonthDay = 'Jun-1')"
      if(month3Input == "1"):
        if(month1Input != "1" and month2Input != "1" and month4Input != "1" and month5Input != "1" and month6Input != "1"):
          message += "t.MonthDay = 'Jul-4'"
        elif(month1Input != "1" and month2Input != "1" and (month4Input == "1" or month5Input == "1" or month6Input == "1")):
          message += "(t.MonthDay = 'Jul-4' OR "
        elif((month2Input == "1" or month1Input == "1") and (month4Input == "1" or month5Input == "1" or month6Input == "1")):
          message += "t.MonthDay = 'Jul-4' OR "
        else:
          message += "t.MonthDay = 'Jul-4')"
      if(month4Input == "1"):
        if(month1Input != "1" and month2Input != "1" and month3Input != "1" and month5Input != "1" and month6Input != "1"):
          message += "t.MonthDay = 'Jul-15'"
        elif(month1Input != "1" and month2Input != "1" and month3Input == "1" and (month5Input == "1" or month6Input == "1")):
          message += "(t.MonthDay = 'Jul-15' OR "
        elif((month2Input == "1" or month1Input == "1" or month3Input == "1") and (month5Input == "1" or month6Input == "1")):
          message += "t.MonthDay = 'Jul-15' OR "
        else:
          message += "t.MonthDay = 'Jul-15')"
      if(month5Input == "1"):
        if(month1Input != "1" and month2Input != "1" and month4Input != "1" and month3Input != "1" and month6Input != "1"):
          message += "t.MonthDay = 'Aug-15'"
        elif(month1Input != "1" and month2Input != "1" and month3Input != "1" and month4Input != "1" and (month6Input == "1")):
          message += "(t.MonthDay = 'Aug-15' OR "
        elif((month2Input == "1" or month1Input == "1" or month3Input == "1" or month4Input == "1") and (month6Input == "1")):
          message += "t.MonthDay = 'Aug-15' OR "
        else:
          message += "t.MonthDay = 'Aug-15')"
      if(month6Input == "1"):
        if(month1Input != "1" and month2Input != "1" and month3Input != "1" and month4Input != "1" and month5Input != "1"):
          message += "t.MonthDay = 'Dec-15'"
        else:
          message += "t.MonthDay = 'Dec-15')"
      whereQuery.append(message)
      """
      if(" OR " in monthInput): #If there are multiple inputs
        splitter = monthInput.split(" OR ")
        for x in splitter:
          if(x == splitter[len(splitter)-1]):
            message += "t.MonthDay = '" + x +"')"
          elif(x == splitter[0]):
            message += "(t.MonthDay = '" + x + "' OR "
          else:  
            message += "t.MonthDay = '" + x + "' OR "
        whereQuery.append(message)
        splitter = []
        message = "("   
      else: #If there is one input 
        whereQuery.append("t.MonthDay = '" + monthInput + "'")
      """
  
  finalQuery = statement[0] + " WHERE "
  #print(whereQuery)
  for x in whereQuery:
    if(x == whereQuery[0]):
      finalQuery += x
    elif(x != ""):
      finalQuery += " AND " + x
  
  cursor2.execute(finalQuery)
  result = cursor2.fetchall()

  #This block prints out the query results
  #heads = ['AcademicID', 'CollegeID', 'SemesterID']
  heads = []
  selectQuery = statement[0].split("FROM")
  selectQuery = selectQuery[0].split(",")
  splits = ""
  for x in selectQuery:
    #if(x == selectQuery[0] or x == selectQuery[1] or x == selectQuery[2]):
      #splits = ""
    #else:
    splits = x
    splits = splits.split('.', 1)
    heads.append(splits[1])
  print(finalQuery)
  print(tabulate(result, headers=heads, tablefmt='psql'))
  print("Returning " + str(len(result)) + " resulting Students in this query.")
  queries.append(finalQuery) 
      
  
def olapPivot(): #Change the Order things are being viewed 
  statement = queries[len(queries)-1]
  if("ORDER BY" in statement):
    realStatement = statement.split("ORDER")
    statement = realStatement[0]

  cnx2 = mysql.connector.connect(user='root',password='password',host='127.0.0.1', database='testschema')
  cursor2 = cnx2.cursor()
  gpaInput = input1.get("1.0", "end-1c")
  statusInput = input2.get("1.0", "end-1c")
  nameInput = input3.get("1.0", "end-1c")
  addressInput = input4.get("1.0", "end-1c")
  gpabox1Input = gpaBox1.get()
  gpabox2Input = gpaBox2.get()
  gpabox3Input = gpaBox3.get()
  collegebox1Input = collegeBox1.get()
  collegebox2Input = collegeBox2.get()
  collegebox3Input = collegeBox3.get()
  collegebox4Input = collegeBox4.get()
  majorInput = input5.get("1.0", "end-1c")
  degreeInput = input6.get("1.0", "end-1c")
  yearInput = input7.get("1.0", "end-1c")
  monthInput = input8.get("1.0", "end-1c")

  element = ""
  if(gpaInput != ""):
    statement += " ORDER BY a.GPA"
  elif(statusInput != ""):
    statement += " ORDER BY a.Status"
  elif(addressInput != ""):
    statement += " ORDER BY a.Address"
  elif(nameInput != ""):
    statement += " ORDER BY a.Name"
  elif(gpabox1Input == "1" or gpabox2Input == "1" or gpabox3Input == "1"):
    statement += " ORDER BY a.gpaQuality"
  elif(collegebox1Input == "1" or collegebox2Input == "1" or collegebox3Input == "1" or collegebox4Input == "1"):
    statement += " ORDER BY p.College"
  elif(majorInput != ""):
    statement += " ORDER BY p.Major"
  elif(degreeInput != ""):
    statement += " ORDER BY p.Degree"
  elif(yearInput != ""):
    statement += " ORDER BY t.Y"
  elif(monthInput != ""):
    statement += " ORDER BY t.MonthDay"
  
  cursor2.execute(statement)
  result = cursor2.fetchall()

  #This block prints out the query results
  heads = ['AcademicID', 'CollegeID', 'SemesterID']
  selectQuery = statement.split("FROM")
  selectQuery = selectQuery[0].split(",")
  splits = ""
  for x in selectQuery:
    if(x == selectQuery[0] or x == selectQuery[1] or x == selectQuery[2]):
      splits = ""
    else:
      splits = x
      splits = splits.split('.', 1)
      heads.append(splits[1])
  print(statement)
  print(tabulate(result, headers=heads, tablefmt='psql'))
  print("Returning " + str(len(result)) + " resulting Students in this query.")
  queries.append(statement) 
  
      
      



"""
Creation of GUI
"""
main = Tk()
#scrollbar = tk.Scrollbar(main)
#scrollbar.pack( side = RIGHT, fill = Y )
query = ("SELECT AcademicID, CollegeID FROM students ")
dimArray = []

var = StringVar()
var.set("")
data=("Rollup", "Rolldown", "Dice", "Slice", "Pivot") #OLAP Operations
options=("0", "1") #Called in GUI creation
cb=Combobox(main, values=data) #Box for OLAP Operations
cb.place(x=40, y=100)
btn=Button(main, text="Start Querying", fg='red', command=lambda:createQuery()) #Submit Button
btn.place(x=550, y=550)
btn2=Button(main, text="Continue Querying", fg='red', command=lambda:continueQuery()) #Contine Cube
btn2.place(x=750, y=550)

label1 = Label(main, text='Commands')
label1.place(x=50, y =70)
label1 = Label(main, text='Dimensions')
label1.place(x=550, y =70)
cursor.execute("SELECT table_name FROM information_schema.tables WHERE table_schema = 'testschema' AND table_name != 'staging' AND table_name != 'students'")
for (table_name) in cursor:
  #print("{}".format(
    #table_name))
  dimArray.append(str(table_name))

dimensionMessage = ""
for x in dimArray:
  #for j, item in enumerate(x):
    #x[j] = item.replace(',', '') Remove , from entries
  dimensionMessage += x + "      "
#print(dimensionMessage)

#Dimensions - These will be edited to work dynamically by final deadline
dim1 = Text(main, height = 5, width = 36, bg='lightgreen')
dim1.insert(END, 'Academics')
dim1.place(x=200, y=175 )
dim2 = Text(main, height = 5, width = 40, bg='lightgreen')
dim2.insert(END, 'Program')
dim2.place(x=500, y=175 )
dim2 = Text(main, height = 5, width = 40, bg='lightgreen')
dim2.insert(END, 'Time')
dim2.place(x=830, y=175 )

cursor.execute("SELECT * FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE_NAME = N'Academics'")
aColumns = []
for (table_name) in cursor:
  aColumns.append(str(table_name))
#print(aColumns)
  
#Columns for Academics
aCol1 = Text(main, height = 10, width = 3, bg='lightgreen')
aCol1.insert(END, 'GPA')
aCol1.place(x=345, y=250 )
input1 = Text(main, height = 3, width = 5, bg='lightyellow')
input1.insert(END, '')
input1.place(x=335, y=430 ) #GPA Filtering
aCol2 = Text(main, height = 10, width = 8, bg='lightgreen')
aCol2.insert(END, 'Status')
aCol2.place(x=200, y=250 )
input2 = Text(main, height = 3, width = 5, bg='lightyellow')
input2.insert(END, '')
input2.place(x=180, y=430 ) #Status Filtering
aCol3 = Text(main, height = 10, width = 5, bg='lightgreen')
aCol3.insert(END, 'Name')
aCol3.place(x=250, y=250 )
input3 = Text(main, height = 3, width = 5, bg='lightyellow')
input3.insert(END, '')
input3.place(x=230, y=430 ) #Name Filtering
aCol4 = Text(main, height = 10, width = 7, bg='lightgreen')
aCol4.insert(END, 'Address')
aCol4.place(x=285, y=250 )
input4 = Text(main, height = 3, width = 5, bg='lightyellow')
input4.insert(END, '')
input4.place(x=285, y=430 ) #Address Filtering
aCol5 = Text(main, height = 6, width = 15, bg='lightgreen')
aCol5.insert(END, 'GPA Quality')
aCol5.place(x=370, y=250 )
aColRow1 = Text(main, height = 4, width = 5, bg='lightgreen')
aColRow1.insert(END, 'high')
aColRow1.place(x=370, y=350)
aColRow2 = Text(main, height = 4, width = 5, bg='lightgreen')
aColRow2.insert(END, 'med')
aColRow2.place(x=410, y=350)
aColRow3 = Text(main, height = 4, width = 5, bg='lightgreen')
aColRow3.insert(END, 'low')
aColRow3.place(x=450, y=350)
gpaBox1=Combobox(main, height = 1, width = 1, values=options)
gpaBox1.place(x=380, y=430)
gpaBox2=Combobox(main, height = 1, width = 1, values=options)
gpaBox2.place(x=420, y=430)
gpaBox3=Combobox(main, height = 1, width = 1, values=options)
gpaBox3.place(x=450, y=430)

#Columns for Program
bCol1 = Text(main, height = 6, width = 28, bg='lightgreen')
bCol1.insert(END, 'College')
bCol1.place(x=500, y=250 )
bColRow1 = Text(main, height = 4, width = 7, bg='lightgreen')
bColRow1.insert(END, 'Cyber')
bColRow1.place(x=500, y=350 )
collegeBox1=Combobox(main, height = 1, width = 1, values=options)
collegeBox1.place(x=500, y=430)
bColRow2 = Text(main, height = 4, width = 7, bg='lightgreen')
bColRow2.insert(END, 'Business')
bColRow2.place(x=545, y=350 )
collegeBox2=Combobox(main, height = 1, width = 1, values=options)
collegeBox2.place(x=545, y=430)
bColRow3 = Text(main, height = 4, width = 7, bg='lightgreen')
bColRow3.insert(END, 'Education')
bColRow3.place(x=604, y=350 )
collegeBox3=Combobox(main, height = 1, width = 1, values=options)
collegeBox3.place(x=604, y=430)
bColRow4 = Text(main, height = 4, width = 7, bg='lightgreen')
bColRow4.insert(END, 'Art and Science')
bColRow4.place(x=662, y=350 )
collegeBox4=Combobox(main, height = 1, width = 1, values=options)
collegeBox4.place(x=662, y=430)
bCol2 = Text(main, height = 10, width = 6, bg='lightgreen')
bCol2.insert(END, 'Major')
bCol2.place(x=720, y=250 )
input5 = Text(main, height = 3, width = 5, bg='lightyellow')
input5.insert(END, '')
input5.place(x=720, y=430 ) #Major Filtering
bCol3 = Text(main, height = 10, width = 6, bg='lightgreen')
bCol3.insert(END, 'Degree')
bCol3.place(x=770, y=250 )
input6 = Text(main, height = 3, width = 5, bg='lightyellow')
input6.insert(END, '')
input6.place(x=770, y=430 ) #Degree Filtering

#Columns for Time
cCol1 = Text(main, height = 10, width = 15, bg='lightgreen')
cCol1.insert(END, 'Year')
cCol1.place(x=830, y=250 )
input7 = Text(main, height = 3, width = 5, bg='lightyellow')
input7.insert(END, '')
input7.place(x=830, y=430 ) #Year Filtering
cCol2 = Text(main, height = 10, width = 25, bg='lightgreen')
cCol2.insert(END, 'MonthDay')
cCol2.place(x=950, y=250 )
#input8 = Text(main, height = 3, width = 5, bg='lightyellow')
#input8.insert(END, '')
#input8.place(x=950, y=430 ) #MonthDay Filtering
cColRow1 = Text(main, height = 4, width = 6, bg='lightgreen')
cColRow1.insert(END, 'Spring')
cColRow1.place(x=950, y=350 )
semesterBox1=Combobox(main, height = 1, width = 1, values=options)
semesterBox1.place(x=960, y=430)
cColRow2 = Text(main, height = 4, width = 3, bg='lightgreen')
cColRow2.insert(END, 'Sum 1')
cColRow2.place(x=1000, y=350 )
semesterBox2=Combobox(main, height = 1, width = 1, values=options)
semesterBox2.place(x=1000, y=430)
cColRow3 = Text(main, height = 4, width = 3, bg='lightgreen')
cColRow3.insert(END, 'Sum 2')
cColRow3.place(x=1025, y=350 )
semesterBox3=Combobox(main, height = 1, width = 1, values=options)
semesterBox3.place(x=1025, y=430)
cColRow4 = Text(main, height = 4, width = 3, bg='lightgreen')
cColRow4.insert(END, 'Sum 3')
cColRow4.place(x=1050, y=350 )
semesterBox4=Combobox(main, height = 1, width = 1, values=options)
semesterBox4.place(x=1050, y=430)
cColRow5 = Text(main, height = 4, width = 3, bg='lightgreen')
cColRow5.insert(END, 'Sum 4')
cColRow5.place(x=1075, y=350 )
semesterBox5=Combobox(main, height = 1, width = 1, values=options)
semesterBox5.place(x=1075, y=430)
cColRow6 = Text(main, height = 4, width = 6, bg='lightgreen')
cColRow6.insert(END, 'Fall')
cColRow6.place(x=1100, y=350 )
semesterBox6=Combobox(main, height = 1, width = 1, values=options)
semesterBox6.place(x=1110, y=430)


message = ""


cursor.close()
cnx.close()
main.geometry("1200x700")
main.mainloop( )



