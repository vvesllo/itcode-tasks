class Human:
    def __init__(self, name, city, birth_year):
        self.name = name
        self.city = city
        self.birth_year = birth_year

    def get_age(self, current_year):
        return current_year - self.birth_year
    

human_1 = Human("Person-A", "Ufa", 2005)

print(human_1.get_age(2024))