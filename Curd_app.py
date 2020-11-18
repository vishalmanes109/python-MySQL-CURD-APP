import mysql.connector
import os
from os.path import join, dirname
from dotenv import load_dotenv

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

HOST = os.environ.get("HOST")
USER = os.environ.get("USER")
DATABASE = os.environ.get("DATABASE")

# creating databse conection instance

mydb = mysql.connector.connect(
  host=HOST,
  user=USER,
  database=DATABASE
)

# creating databse cursor
cursor = mydb.cursor()

# add employee method
def addemployee(ename,eadd,edob,emobile):
  print("Adding Employee in to databse...")
  sql = "INSERT INTO Employee (ename,eaddress,edob,emobile) VALUES ( %s,%s,%s,%s)"
  val = (ename,eadd,edob,emobile)

  cursor.execute(sql, val)

  mydb.commit()

  print(cursor.rowcount, "record inserted.")
  print("Employee Added")

def deleteemployee(ename,eid):
  print("Deleting Employee...")
  sql = "DELETE FROM employee WHERE eid = %s"
  eid = (eid,)
  cursor.execute(sql, eid)

  mydb.commit()

  print(cursor.rowcount, "record(s) deleted")
  print("Employee Deleted")


def updateeployee(ename,eid):
  print("Enter 1: to Update  Address")
  print("Enter 2: to Update DOB ")
  print("Enter 3: to Update Mobile no. ")
  sel = int(input("Enter choice: "))

  if (sel==1):
    eaddress = input("Enter The new address: ").strip().title()
    print("updating Employee")

    sql = "UPDATE employee SET eaddress = %s WHERE eid = %s"
    val = (eaddress, eid)

    cursor.execute(sql, val)

    mydb.commit()

    print(cursor.rowcount, "record(s) affected")
    print("employee Updated")

  elif(sel==2):
    edob = input("Enter The new DOB (YY-MM-DD): ").strip()

    print("updating Employee")

    sql = "UPDATE employee SET edob = %s WHERE eid = %s"
    val = (edob, eid)

    cursor.execute(sql, val)

    mydb.commit()

    print(cursor.rowcount, "record(s) affected")
    print("employee Updated") 
    
  elif(sel==3):
    emobile = input("Enter The new Mobile No : ").strip()

    print("updating Employee")

    sql = "UPDATE employee SET emobile = %s WHERE eid = %s"
    val = (emobile, eid)

    cursor.execute(sql, val)

    mydb.commit()

    print(cursor.rowcount, "record(s) affected")
    print("employee Updated")



def searchemployee():
  
  print("\nEnter 1: to Search By ID")
  print("Enter 2: to Search By Name")
  print("Enter 3: to Search By  Age\n")
  sel = int(input("Enter choice: "))
  if(sel == 1):
    eid = int(input("Enter Emp id: "))
    
    sql = ("SELECT * FROM employee where eid=%s")
    eid=(eid,)
    cursor.execute(sql, eid)
    res = cursor.fetchall()
    if(len(res)==0):
      print("No record Found")
    else:    
      for emp in res:
        print("**Employee Details**")
        print("id: ", emp[0] )
        print("name :",emp[1])
        print("address: ",emp[2])
        print("DOB: ",emp[3])
        print("Mobile No: ",emp[4])
        print("**END**")

  elif(sel == 2):
    ename = input("Enter Name of Employee which has to be search: ").strip().title()
    sql = ("SELECT * FROM employee where ename=%s")
    ename=(ename,)
    cursor.execute(sql, ename)
    res = cursor.fetchall()

    if(len(res) == 0):
      print("No record Found")
    else:
      print(len(res)," Employee Found")
      for emp in res:
        print("**Employee Details**")
        print("id: ", emp[0])
        print("name :", emp[1])
        print("address: ", emp[2])
        print("DOB: ", emp[3])
        print("Mobile No: ", emp[4])
        print("**END**")

  elif(sel == 3):
    emobile = input("Enter Mobile no  of Employee which has to be Search: ")
    sql = ("SELECT * FROM employee where emobile=%s")
    emobile=(emobile,)
    cursor.execute(sql, emobile)
    res = cursor.fetchall()

    if(len(res) == 0):
      print("No record Found")
    else:
      for emp in res:
        print("**Employee Details**")
        print("id: ", emp[0])
        print("name :", emp[1])
        print("address: ", emp[2])
        print("DOB: ", emp[3])
        print("Mobile No: ", emp[4])
        print("**END**")

  else:
    print("Enter Valid choice for searching")
      
    


#addemployee()  

#deleteemployee()
#updateeployee()
#searchemployee()


def menu():
  """
  1. ADD
  2.Update
  3.DELETE
  4.SEARCH
  """

  while(True):
    print("\nEnter 1: ADD Employee")
    print("Enter 2: Update Employee")
    print("Enter 3: Delete Employee")
    print("Enter 4: Search Employee")
    print("Enter 9: Exit\n")
    choice = int(input("Enter Your Choice: ").strip())

    if(choice == 1):
      ename = input("Enter Name: ").strip().title()
      eadd = input("Enter Address: ").strip().title()
      edob = input("Enter Date Of Birth (YY-MM-DD): ").strip()
      emobile = input("ENter Mobile No: ").strip()
      addemployee(ename, eadd, edob, emobile)
    elif(choice == 2):
      ename = input(
          "Enter Name of employee which has to be updated: ").strip().title()
      eid = int(input("Enter Emp id: "))
      updateeployee(ename, eid)

    elif(choice == 3):
      ename = input(
          "Enter Name of Employee which has to be deleted: ").strip().title()
      eid = int(input("Enter Emp id: "))
      deleteemployee(ename, eid)

    elif(choice == 4):
      searchemployee()

    elif(choice==9):
      print("Thanks ")
      break  

    else:
      print("Enter proper choice ")

print("\n*****Welocome to employee Database Management*******")
print(" ")
menu()
