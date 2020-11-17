import mysql.connector

# creating databse conection instance

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  database="curd_app"
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
  eaddress=input("Enter The new address")

  print("updating Employee")

  sql = "UPDATE employee SET eaddress = %s WHERE eid = %s"
  val = (eaddress, eid)

  cursor.execute(sql, val)

  mydb.commit()

  print(cursor.rowcount, "record(s) affected")
  print("employee Updated")


def searchemployee():
  
  print("Enter 1: to Search By ID")
  print("Enter 2: to Search By name")
  print("Enter 3: to Search By mobile no")
  sel = int(input("Enter choice: "))
  if(sel == 1):
    eid = int(input("Enter Emp id "))
    sql = ("SELECT * FROM employee where eid=%s")
    eid=(eid,)
    cursor.execute(sql, eid)
    res = cursor.fetchall()
      
    for emp in res:
      print(emp)

  elif(sel == 2):
    ename = input("Enter Name of Employee which has to be search")
    sql = ("SELECT * FROM employee where eid=%s")
    ename=(ename,)
    cursor.execute(sql, ename)
    res = cursor.fetchall()

    for emp in res:
      print(emp)

  elif(sel == 3):
    emobile = input("Enter Mobile no  of Employee which has to be Search")
    sql = ("SELECT * FROM employee where emobile=%s")
    emobile=(emobile,)
    cursor.execute(sql, emobile)
    res = cursor.fetchall()

    for emp in res:
      print(emp)

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
    print("Enter 1: ADD Employee")
    print("Enter 2: Update Employee")
    print("Enter 3: Delete Employee")
    print("Enter 4: Search Employee")
    print("Enter 9: Exit")
    choice = int(input("Enter Your Choice: ").strip())

    if(choice == 1):
      ename = input("Enter Name: ").strip()
      eadd = input("Enter Address: ").strip()
      edob = input("Enter Date Of Birth: ").strip()
      emobile = input("ENter Mobile No: ").strip()
      addemployee(ename, eadd, edob, emobile)
    elif(choice == 2):
      ename = input("Enter Name of employee which has to be updated: ")
      eid = int(input("Enter Emp id: "))
      updateeployee(ename, eid)

    elif(choice == 3):
      ename = input("Enter Name of Employee which has to be deleted: ")
      eid = int(input("Enter Emp id: "))
      deleteemployee(ename, eid)

    elif(choice == 4):
      searchemployee()

    elif(choice==9):
      print("Thanks ")
      break  

    else:
      print("Enter proper choice: ")

print("*****Welocome to employee Database Management*******")
print(" \n\n")
menu()
