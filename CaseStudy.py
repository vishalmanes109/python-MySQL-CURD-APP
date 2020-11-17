class Employee:
    def __init__(self, eID, eName, eAddress, eDOB, eMob):
        self.employeeID=eID
        self.employeeName=eName
        self.employeeAddress=eAddress
        self.employeeDOB=eDOB
        self.employeeMobile=eMob

    def getEmpID(self):
        return self.employeeID


    def getEmpAddress(self):
        return self.employeeAddress
    

    def getEmpName(self):
        return self.employeeName
    

    def getEmpDOB(self):
        return self.employeeDOB
        
    def getEmpMobile(self):
        return self.employeeMobile


    def setEmpName(self, newName):
        self.employeeName = newName
    
    
    def AddEmployee(self,newEmp):
        self.EmployeeList.append(newEmp)

    def UpdateEmployee(self,employeeID,newEmpName):
        for i in self.EmployeeList:
            if(i.getEmpID()==employeeID):
                i.setEmpName(newEmpName)
                i.employeeName=newEmpName

    def DeleteEmpoyee(self, employeeID):
        temp = self.EmployeeList.pop[employeeID]
        return EmployeeList
    
    def SearchEmployee(self, employeeID):
        for i in self.EmployeeList:
            if(i.getEmpID()==employeeID):
                return i.getEmpName()
                
                

