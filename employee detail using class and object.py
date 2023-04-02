class Employee:
	__id=0
	__name=""
	__gender=""
	__city=""
	__salary=0
	def setData(self):
		self.__id=int(input("Enter Id\t:"))
		self.__name = input("Enter Name\t:")
		self.__gender = input("Enter Gender:")
		self.__city = input("Enter City\t:")
		self.__salary = int(input("Enter Salary:"))
	def showData(self):
		print("Id\t\t:",self.__id)
		print("Name\t:", self.__name)
		print("Gender\t:", self.__gender)
		print("City\t:", self.__city)
		print("Salary\t:", self.__salary)

emp=Employee()
emp.setData()
emp.showData()
