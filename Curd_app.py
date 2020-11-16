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
def addemployee():
  print("Adding Employee in to databse...")
  sql = "INSERT INTO Employee (ename,eaddress,edob,emobile) VALUES ( %s,%s,%s,%s)"
  val = ("Jayesh", "Vashi ","4/1/1987","84278747598")

  cursor.execute(sql, val)

  mydb.commit()

  print(cursor.rowcount, "record inserted.")
  print("Employee Added")

def deleteemployee():
  print("Deleting Employee...")
  sql = "DELETE FROM employee WHERE ename = %s"
  adr = ("Vishal", )
  cursor.execute(sql, adr)

  mydb.commit()

  print(cursor.rowcount, "record(s) deleted")
  print("Employee Deleted")


def updateeployee():
  print("updating Employee")
  sql = "UPDATE employee SET eaddress = %s WHERE eaddress = %s"
  val = ("Mumbai", "Highway 121")

  cursor.execute(sql, val)

  mydb.commit()

  print(cursor.rowcount, "record(s) affected")
  print("employee Updated")


def searchemployee():
  sql=("SELECT * FROM employee where ename=%s")
  ename=("Jayesh",)
  cursor.execute(sql, ename)
  res = cursor.fetchall()

  for emp in res:
    print(emp)



#addemployee()  

#deleteemployee()
#updateeployee()
searchemployee()
