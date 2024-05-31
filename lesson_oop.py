

class Human:
    def __init__(self, name, age):
        self.name = name
        self.age = age


class Teacher(Human):
    def __init__(self, name, age, science):
        super().__init__(name, age)
        self.science = science

    def teach(self):
        print(f'Teaching {self.science}')


class Director(Teacher, Human):
    def __init__(self, name, age, science):
        super().__init__(name, age, science)

    def __str__(self):
        return 'ЭТО ДИРЕКТОР!'


d = Director('a', 24, 'history')

print(d.science)
d.teach()
print(d)