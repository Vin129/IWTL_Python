class BTreeNode:
    Value = None;
    Left = None;
    Right = None;
    Depth = None;
    def __init__(self,v:int):
        self.Value = v;

class AVLTree:
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
            Node.Depth = 0
        else:
            if Node.Value > X :
                Node.Left = self.__add(Node.Left,X)
                if self.GetDepth(Node.Left) - self.GetDepth(Node.Right) == 2:
                    if Node.Left.Value > X:
                        Node = self.SingleRotateRight(Node) # 左-左型
                    else:
                        Node = self.DoubleRotateLeft(Node) # 左-右型
            elif Node.Value < X:
                Node.Right = self.__add(Node.Right,X)
                if self.GetDepth(Node.Right) - self.GetDepth(Node.Left) == 2:
                    if Node.Right.Value < X:
                        Node = self.SingleRotateLeft(Node) # 右-右型
                    else:
                        Node = self.DoubleRotateRight(Node) # 右-左型

        Node.Depth = (self.GetDepth(Node.Right) if self.GetDepth(Node.Left) < self.GetDepth(Node.Right) else self.GetDepth(Node.Left)) + 1
        return Node

    def GetDepth(self,Node:BTreeNode) -> int:
        if Node == None:
            return -1;
        return Node.Depth

    #右-右型：左旋 父节点被自己的右孩子取代，右孩子的左子节点变成自己的右孩子，而自己成为自己的左孩子
    def SingleRotateLeft(self,Node:BTreeNode) -> BTreeNode:
        TempNode = Node
        Node = TempNode.Right
        TempNode.Right = Node.Left
        TempNode.Depth = (self.GetDepth(TempNode.Right) if self.GetDepth(TempNode.Left) < self.GetDepth(
            TempNode.Right) else self.GetDepth(TempNode.Left)) + 1
        Node.Left = TempNode
        Node.Depth = (self.GetDepth(Node.Right) if self.GetDepth(Node.Left) < self.GetDepth(
            Node.Right) else self.GetDepth(Node.Left)) + 1
        return Node

    # 左-左型：右旋  父节点被自己的左孩子取代，左孩子的右子节点变成自己的左孩子，而自己成为自己的右孩子
    def SingleRotateRight(self,Node:BTreeNode)-> BTreeNode:
        TempNode = Node
        Node = TempNode.Left
        TempNode.Left = Node.Right
        TempNode.Depth = (self.GetDepth(TempNode.Right) if self.GetDepth(TempNode.Left) < self.GetDepth(
            TempNode.Right) else self.GetDepth(TempNode.Left)) + 1
        Node.Right = TempNode
        Node.Depth = (self.GetDepth(Node.Right) if self.GetDepth(Node.Left) < self.GetDepth(
            Node.Right) else self.GetDepth(Node.Left)) + 1
        return Node

    # 左-右型  先对左子节点进行左旋,后对父节点右旋
    def DoubleRotateLeft(self,Node:BTreeNode) -> BTreeNode:
        Node.Left = self.SingleRotateLeft(Node.Left)
        return self.SingleRotateRight(Node)

    # 右-左型  先对右子节点进行右旋,后对父节点左旋
    def DoubleRotateRight(self, Node: BTreeNode) -> BTreeNode:
        Node.Right = self.SingleRotateRight(Node.Right)
        return self.SingleRotateLeft(Node)

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


AVL = AVLTree()
A = [3,2,1,4,5,6,7,10,9,8]
for x in A:
    AVL.Add(x);

AVL.Log()
