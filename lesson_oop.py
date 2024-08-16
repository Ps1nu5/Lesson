'''
Это третье практическое задание (03) к шестому модулю (06) "Наследование классов".

Домашнее задание по теме "Множественное наследование".
Цель: закрепить знания множественного наследования в Python.

Задача "Мифическое наследование":

Необходимо написать 3 класса:

    Horse - класс, описывающий лошадь. Объект этого класса обладает следующими атрибутами:
        1. x_distance = 0 - пройденный путь.
        2. sound = 'Frrr' - звук, который издаёт лошадь.

        И методами:
        1. run(self, dx), где dx - изменение дистанции, увеличивает x_distance на dx.

    Eagle - класс описывающий орла. Объект этого класса обладает следующими атрибутами:
        1. y_distance = 0 - высота полёта
        2. sound = 'I train, eat, sleep, and repeat' - звук, который издаёт орёл (отсылка)

        И методами:
        1. fly(self, dy) где dy - изменение дистанции, увеличивает y_distance на dy.

    Pegasus - класс описывающий пегаса. Наследуется от Horse и Eagle в том же порядке.
        Объект такого класса должен обладать атрибутами классов родителей в порядке наследования.

        Также обладает методами:
        1. move(self, dx, dy) - где dx и dy изменения дистанции. В этом методе должны запускаться
           наследованные методы run и fly соответственно.
        2. get_pos(self) возвращает текущее положение пегаса в виде кортежа -
           (x_distance, y_distance) в том же порядке.
        3. voice - который печатает значение унаследованного атрибута sound.

Пункты задачи:
    1. Создайте классы родители: Horse и Eagle с методами из описания.
    2. Создайте класс наследник Pegasus с методами из описания.
    3. Создайте объект класса Pegasus и вызовите каждый из ранее перечисленных методов, проверив их работу.

Пример результата выполнения программы:

Пример работы программы:
p1 = Pegasus()

print(p1.get_pos())
p1.move(10, 15)
print(p1.get_pos())
p1.move(-5, 20)
print(p1.get_pos())

p1.voice()

Вывод на консоль:
(0, 0)
(10, 15)
(5, 35)
I train, eat, sleep, and repeat

Примечания:
    1. Будьте внимательней, когда вызываете методы классов родителей в классе наследнике
       при множественном наследовании: при обращении через super() методы будут искаться сначала в первом,
       потом во втором и т.д. классах по mro().
    2. Заметьте, что Pegasus издаёт звук "I train, eat, sleep, and repeat",
       т.к. по порядку сначала идёт наследование от Horse, а после от Eagle.
'''

print()

class Horse():
    '''
    'Horse' - класс, описывающий лошадь. Объект этого класса обладает следующими атрибутами:
        1. 'x_distance' = 0 - пройденный путь.
        2. 'sound' = 'Frrr' - звук, который издаёт лошадь.

        И методами:
        1. 'run(self, dx)', где 'dx' - изменение дистанции, увеличивает 'x_distance' на 'dx'.
    '''
    x_distance = 0
    sound = 'Frrr'

    def __init__(self, x_distance = x_distance, sound = sound):
        self.x_distance = x_distance
        self.sound = sound
        super().__init__()
        pass

    def run(self, dx):
        self.x_distance += dx
        return self.x_distance
        pass
    pass

class Eagle():
    '''
    'Eagle' - класс описывающий орла. Объект этого класса обладает следующими атрибутами:
        1. 'y_distance' = 0 - высота полёта
        2. 'sound' = 'I train, eat, sleep, and repeat' - звук, который издаёт орёл (отсылка)

        И методами:
        1. 'fly(self, dy)' где dy - изменение дистанции, увеличивает 'y_distance' на 'dy'.
    '''
    y_distance = 0
    sound = 'I train, eat, sleep, and repeat'

    def __init__(self, y_distance = y_distance, sound = sound):
        self.y_distance = y_distance
        self.sound = sound
        pass

    def fly(self, dy):
        self.y_distance += dy
        return self.y_distance
        pass
    pass

class Pegasus(Horse, Eagle):
    '''
    'Pegasus' - класс описывающий пегаса. Наследуется от 'Horse' и 'Eagle' в том же порядке.
        Объект такого класса должен обладать атрибутами классов родителей в ПОРЯДКЕ НАСЛЕДОВАНИЯ.

        Также обладает методами:
        1. 'move(self, dx, dy)' - где 'dx' и 'dy' изменения дистанции. В этом методе должны запускаться
           наследованные методы 'run' и 'fly' соответственно.
        2. 'get_pos(self)' возвращает текущее положение пегаса в виде кортежа -
           ('x_distance', 'y_distance') в том же порядке.
        3. 'voice' - который печатает значение унаследованного атрибута 'sound'.
    '''
    def __init__(self):
        #Horse.__init__(self)
        #Eagle.__init__(self)
        super().__init__()
        pass

    def move(self, dx, dy):
        self.x_distance = self.run(dx)
        self.y_distance = self.fly(dy)
        pass

    def get_pos(self):
        return (self.x_distance, self.y_distance)
        pass

    def voice(self):
        print(self.sound)
        pass
    pass

# Пример работы программы:

# Код для проверки:
p1 = Pegasus()

print(p1.get_pos())
p1.move(10, 15)
print(p1.get_pos())
p1.move(-5, 20)
print(p1.get_pos())

p1.voice()

# Вывод на консоль:
'''
(0, 0)
(10, 15)
(5, 35)
I train, eat, sleep, and repeat
'''
