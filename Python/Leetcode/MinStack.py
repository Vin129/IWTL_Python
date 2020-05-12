#155
class MinStack:
    head = None
    num = 0
    def __init__(self):
        self.__lst = []
        self.head = None


    def push(self, x: int) -> None:
        self.__lst.append(x)
        self.head = self.__lst[-1]
        self.num = self.num + 1

    def pop(self) -> None:
        if self.num == 0:
            return None
        re = self.head
        del self.__lst[-1]
        self.num = self.num - 1
        if self.num == 0:
            self.head = None
        else:
            self.head = self.__lst[-1]
        return re

    def top(self) -> int:
        return self.head

    def getMin(self) -> int:
        if self.num == 0:
            return None
        return min(self.__lst)