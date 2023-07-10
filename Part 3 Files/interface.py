#Created By: James Kyle Harrison
#
#Requires mysql-connector-python
import datetime
import mysql.connector
from tkinter import *
from tkinter.ttk import Combobox
import array as arr

cnx = mysql.connector.connect(user='root',password='password',host='127.0.0.1', database='testschema')
cursor = cnx.cursor()


def createQuery(): #Used in obtaining Data for OLAP to SQL Query Conversion
  cnx2 = mysql.connector.connect(user='root',password='password',host='127.0.0.1', database='testschema')
  cursor2 = cnx2.cursor()
  selectQuery = ["SELECT s.AcademicID, s.CollegeID, s.SemesterID "]
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
  monthInput = input8.get("1.0", "end-1c")

  if(gpaInput != "" or statusInput != "" or nameInput != "" or addressInput != "" or gpabox1Input != "" or gpabox2Input != "" or gpabox3Input != ""):
    fromQuery.append("academics a")
    whereQuery.append("a.AcademicID = s.AcademicID")
    if(gpaInput != ""):
      whereQuery.append("a.GPA = " + gpaInput)
    if(statusInput != ""):
      whereQuery.append("a.Status = " + statusInput)
    if(addressInput != ""):
      whereQuery.append("a.Address = " + addressInput)
    if(gpabox1Input == "1"):
      whereQuery.append("a.gpaQuality = 'high'")
    if(gpabox2Input == "1"):
      whereQuery.append("a.gpaQuality = 'medium'")
    if(gpabox3Input == "1"):
      whereQuery.append("a.gpaQuality = 'low'")
  if(collegebox1Input != "" or collegebox2Input != "" or collegebox3Input != "" or collegebox4Input != "" or majorInput != "" or degreeInput != ""):
    fromQuery.append("program p")
    whereQuery.append("p.CollegeID = s.CollegeID")
    if(collegebox1Input == "1"):
      whereQuery.append("p.College = 'Cyber College'")
    if(collegebox2Input == "1"):
      whereQuery.append("p.College = 'College of Business'")
    if(collegebox3Input == "1"):
      whereQuery.append("p.College = 'College of Education'")
    if(collegebox4Input == "1"):
      whereQuery.append("p.College = 'College of Art of Science'")
    if(majorInput != ""):
      whereQuery.append("p.Major = " + majorInput)
    if(degreeInput != ""):
      whereQuery.append("p.Degree = " + degreeInput)    
  if(yearInput != "" or monthInput != ""):
    fromQuery.append("time t")
    whereQuery.append("t.SemesterID = s.SemesterID")
    if(yearInput != ""):
      whereQuery.append("t.Y = " + yearInput)
    if(monthInput != ""):
      whereQuery.append("t.MonthDay = " +monthInput)
  finalQuery = selectQuery[0]
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
  for (AcademicID, CollegeID, SemesterID) in cursor2:
    print("{}, {}, {}".format(
      AcademicID, CollegeID, SemesterID))




  

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
btn=Button(main, text="Submit", fg='red', command=lambda:createQuery()) #Submit Button
btn.place(x=550, y=550)

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

print(dimensionMessage)

#Dimensions - These will be edited to work dynamically by final deadline
dim1 = Text(main, height = 5, width = 36, bg='lightgreen')
dim1.insert(END, 'Academics')
dim1.place(x=200, y=175 )
dim2 = Text(main, height = 5, width = 40, bg='lightgreen')
dim2.insert(END, 'Program')
dim2.place(x=500, y=175 )
dim2 = Text(main, height = 5, width = 30, bg='lightgreen')
dim2.insert(END, 'Time')
dim2.place(x=850, y=175 )

cursor.execute("SELECT * FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE_NAME = N'Academics'")
aColumns = []
for (table_name) in cursor:
  aColumns.append(str(table_name))
#print(aColumns)
  
#Columns for Academics - These will be edited to work dynamically by final deadline
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
cCol1.place(x=850, y=250 )
input7 = Text(main, height = 3, width = 5, bg='lightyellow')
input7.insert(END, '')
input7.place(x=850, y=430 ) #Year Filtering
cCol2 = Text(main, height = 10, width = 15, bg='lightgreen')
cCol2.insert(END, 'MonthDay')
cCol2.place(x=970, y=250 )
input8 = Text(main, height = 3, width = 5, bg='lightyellow')
input8.insert(END, '')
input8.place(x=970, y=430 ) #MonthDay Filtering



cursor.execute(query)
message = ""


for (AcademicID, CollegeID) in cursor:
  print("{}, {}".format(
    AcademicID, CollegeID))
  #message += str(AcademicID) + " , " + CollegeID + "\n"

cursor.close()
cnx.close()
#messageVar = Message(main, text = message)
#messageVar.config(bg='lightgreen')
#messageVar.pack( )
main.geometry("1200x700")
main.mainloop( )



