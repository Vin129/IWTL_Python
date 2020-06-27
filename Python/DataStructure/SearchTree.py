class BTreeNode:
    Value = None;
    Left = None;
    Right = None;
    def __init__(self,v:int):
        self.Value = v;

# 二叉搜索树   左子树值一定小于其根节点的值，右子树的值一定大于根节点的值
class SearchTree:
    Node = None

    def Find(self,X:int) -> BTreeNode:
        self.__find(self.Node,X)

    def __find(self,Node:BTreeNode,X:int):
        if Node == None :
            return None;
        if Node.Value == X:
            return Node
        if Node.Value > X:
            return self.__find(Node.Left,X);
        return self.__find(Node.Right,X);

    def Add(self,X:int):
        self.Node = self.__add(self.Node,X);

    def __add(self,Node:BTreeNode,X:int) -> BTreeNode:
        if Node == None:
            Node = BTreeNode(X)
        else:
            if Node.Value > X :
                Node.Left = self.__add(Node.Left,X)
            elif Node.Value < X:
                Node.Right = self.__add(Node.Right, X)
        return  Node

    # 删除操作：叶子就直接删除，存在一个子节点则连接上下，若存在两个，则将该节点右侧的最小值（叶子）替代该节点的值，并删除叶子。
    def Delete(self,X:int):
        self.__delete(self.Node,X);

    def __delete(self,Node:BTreeNode,X:int) -> BTreeNode:
        if Node == None:
            return None;
        if Node.Value > X:
            Node.Left = self.__delete(Node.Left,X)
        elif Node.Value < X:
            Node.Right = self.__delete(Node.Right,X)
        elif Node.Value == X:
            if Node.Left != None and Node.Right != None:
                v = self.__getMin(Node.Right);
                Node.Value = v
                Node.Right = self.__delete(Node.Right,v) # 替换了右子树的最小值后删除该最小值的叶子节点。
            else:
                if Node.Left == None:
                    Node = Node.Right;
                elif Node.Right == None:
                    Node = Node.Left;
        return Node

    # 最小值就是左侧叶子
    def GetMin(self) -> int:
        return self.__getMin(self.Node)
    def __getMin(self,Node) -> int:
        if Node == None:
            return None;
        if Node.Left == None:
            return Node.Value;
        return self.__getMin(Node.Left);

    # 最大值就是右侧叶子
    def GetMax(self) -> int:
        return self.__getMax(self.Node)
    def __getMax(self,Node) -> int:
        if Node == None:
            return None;
        if Node.Right == None:
            return Node.Value;
        return self.__getMax(Node.Right);

    def Log(self):
        self.__log(self.Node,0)
    def __log(self,Node:BTreeNode,depth:int):
        empty = "  "
        if (Node == None):
            return;
        if (Node.Value == None):
            print(empty * depth + "N")
        else:
            print(empty * depth + str(Node.Value))
        if (Node.Left != None):
            self.__log(Node.Left, depth + 1);
        if (Node.Right != None):
            self.__log(Node.Right, depth + 1);

ST = SearchTree();
A = [6,2,1,4,3,8]
# A = [5,8,7,61,445,7,5,7,1315,7,674,1,34,6132,446,7,54,723,41,0,16,41]
for x in A:
    ST.Add(x);
# ST.Delete(4)
# ST.Delete(6132)
print(ST.GetMin())
print(ST.GetMax())
ST.Log()
