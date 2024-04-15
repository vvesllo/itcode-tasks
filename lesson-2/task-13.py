students = {'Schultz', 'Django', 'Brunhilde', 'Fritz'}
employees = {'Schultz', 'Django', 'Calvin', 'Butch', 'Fritz'}

students_employees_1 = students & employees
everyone_1 = students | employees

students_employees_2 = students.intersection(employees)
everyone_2 = students.union(employees)

print("Все люди(1):", ", ".join(everyone_1))
print("Все люди(2):", ", ".join(everyone_2))
print("Учатся и работают(1):", ", ".join(students_employees_1))
print("Учатся и работают(2):", ", ".join(students_employees_2))
print("Только учатся:", ", ".join(students))
print("Только работают:", ", ".join(employees))
