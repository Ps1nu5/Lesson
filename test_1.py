class Test():
    __x = 2
    __y = 5

    def get_coord(self):
        return self.__x, self.__y


a = Test()
print(a.get_coord())
