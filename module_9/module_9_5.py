

class StepValueError(ValueError):
    pass


class Iterator:
    def __init__(self, start, stop, step=1):
        self.step = step
        self.stop = stop
        self.start = start
        self.pointer = self.start
        self.__is_valid_step(self.step)

    def __is_valid_step(self, number):
        if number == 0:
            raise StepValueError('шаг не может быть равен 0')
        return True

    def __iter__(self):
        self.pointer = self.start
        return self

    def __next__(self):
        current_value = self.pointer
        if (self.pointer > self.stop and self.step > 0) or (self.pointer < self.stop and self.step < 0):
            raise StopIteration
        self.pointer += self.step
        return current_value


try:
    iter1 = Iterator(100, 200, 0)
    for i in iter1:
        print(i, end=' ')
except StepValueError:
    print('Шаг указан неверно')

iter2 = Iterator(-5, 1)
iter3 = Iterator(6, 15, 2)
iter4 = Iterator(5, 1, -1)
iter5 = Iterator(10, 1)


for i in iter2:
    print(i, end=' ')
print()
for i in iter3:
    print(i, end=' ')
print()
for i in iter4:
    print(i, end=' ')
print()
for i in iter5:
    print(i, end=' ')
print()
