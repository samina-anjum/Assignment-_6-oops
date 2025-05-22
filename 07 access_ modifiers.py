

class Employee:
    def __init__(self,name,salary,ssn):
        self.name=name#public
        self._salary=salary#protected
        self._ssn=ssn#private

emp = Employee("samina",70000,"03003654762")      
        
print(emp.name)
print(emp._salary)
print(emp.__ssn)