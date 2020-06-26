class EasyListNode:
    Value = None;
    Next = None;
    def __init__(self,value:int):
        self.Value = value;

class EasyList:
    List = None;
    __temp = None;
    def __init__(self):
        self.List = EasyListNode(None);

    def IsEmpty(self):
        return self.List.Value == None;

    def IsLast(self,Node:EasyListNode):
        return Node.Next == None;

    def FindByValue(self,value:int) -> EasyListNode:
        if(self.IsEmpty()):
            return self.List;
        else:
            self.__temp = self.List;
            while(self.__temp != None and self.__temp.Value != value):
                self.__temp = self.__temp.Next;
        return self.__temp;

    def FindByPosition(self,pos:int) -> EasyListNode:
        if(self.IsEmpty()):
            return self.List;
        else:
            num = 0;
            self.__temp = self.List;
            while(self.__temp != None and num != pos):
                self.__temp = self.__temp.Next;
                num += 1;
        return self.__temp;


    def AddEnd(self,X:int):
        if self.List.Value == None:
            self.List.Value = X;
        else:
            self.__temp = self.List;
            while(self.__temp.Next != None):
                self.__temp = self.__temp.Next;
            self.__temp.Next = EasyListNode(X);

    def Add(self,X:int,value:int):
        node = self.FindByValue(value)
        if node == None:
            return;
        if node.Value == None:
            node.Value = X;
            return;
        node.Next = EasyListNode(X);

    def Delete(self,pos:int):
        if self.IsEmpty():
            return;
        if pos == 0:
            self.List = self.List.Next;
            return;
        node = self.FindByPosition(pos-1);
        if node == None or node.Value == None:
            return;
        self.__temp = node.Next;
        node.Next = self.__temp.Next;

    def Print(self):
        self.__temp = self.List;
        while(self.__temp != None and self.__temp.Value != None):
            print(self.__temp.Value);
            self.__temp = self.__temp.Next;



easyList = EasyList();
easyList.AddEnd(1);
easyList.AddEnd(3);
easyList.AddEnd(5);
easyList.AddEnd(8);
easyList.Print();
easyList.Delete(1);
easyList.Print();



