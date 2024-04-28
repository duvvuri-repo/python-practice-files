class Employee:
    def __init__(self,id,name):
        self.id=id
        self.name=name
    def display(self):
        print(f"Employee: {self.name} Id: {self.id}")
# object creation for class Employee
emp=Employee(101,"Amithab")
# calling display method
#emp.display()

# deleting the property of object
del emp.id
try:
    print(emp.id)
except Exception as e:
    print(f"{type(e).__name__}: {e}")

#deleting the object itself
del emp
try:
    emp.display()
except Exception as e:
    #print(e)
    print(f"{type(e).__name__}: {e}")

