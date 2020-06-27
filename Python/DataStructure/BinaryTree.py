#二叉树
class BTreeNode:
    Value = None;
    Left = None;
    Right = None;
    def __init__(self,v:int):
        self.Value = v;


def ForeachTree(Node:BTreeNode):
    ListOfTree3(Node, 0);

# 先序
def ListOfTree(Node:BTreeNode,depth:int):
    empty = "  "
    if(Node.Value == None):
        print(empty*depth + "N")
    else:
        print(empty*depth + str(Node.Value))
    if(Node.Left != None):
        ListOfTree(Node.Left,depth + 1);
    if(Node.Right != None):
        ListOfTree(Node.Right,depth + 1);

# 中序
def ListOfTree2(Node:BTreeNode,depth:int):
    empty = "  "
    if(Node.Left != None):
        ListOfTree2(Node.Left,depth + 1);
    if(Node.Value == Node):
        print(empty*depth + "N")
    else:
        print(empty*depth + str(Node.Value))
    if(Node.Right != None):
        ListOfTree2(Node.Right,depth + 1);

# 后序
def ListOfTree3(Node:BTreeNode,depth:int):
    empty = "  "
    if(Node.Left != None):
        ListOfTree3(Node.Left,depth + 1);
    if (Node.Right != None):
        ListOfTree3(Node.Right, depth + 1);
    if(Node.Value == Node):
        print(empty*depth + "N")
    else:
        print(empty*depth + str(Node.Value))



N = BTreeNode("+")
N.Left = BTreeNode("+")
N.Right = BTreeNode("-")
N.Left.Left = BTreeNode(1)
N.Left.Right = BTreeNode("*")
N.Left.Right.Left = BTreeNode(2)
N.Left.Right.Right = BTreeNode(3)
N.Right.Left = BTreeNode(4)
N.Right.Right = BTreeNode("/")
N.Right.Right.Left = BTreeNode(5)
N.Right.Right.Right = BTreeNode(6)
ForeachTree(N)
