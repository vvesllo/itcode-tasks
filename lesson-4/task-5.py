class Employee:
    def get_paid(self):
        return 10

class Manager(Employee):
    def get_paid(self):
        return 1000


class Worker(Employee):
    def get_paid(self):
        return 2000
    
a = Manager()
b = Worker()

print(a.get_paid())
print(b.get_paid())