class TreeNode:
    Value = None;
    FirstChild = None; # 第一个子节点
    NextSibling = None; # 右侧下一个兄弟
    def __init__(self,v:int):
        self.Value = v;

def ForeachTree(Node:TreeNode):
    ListOfTree(Node, 0);
    print("======================")
    ListOfTree2(Node,0);

# 先序
def ListOfTree(Node:TreeNode,depth:int):
    empty = "  "
    if(Node.Value == Node):
        print(empty*depth + "N")
    else:
        print(empty*depth + str(Node.Value))
    if(Node.FirstChild != None):
        ListOfTree(Node.FirstChild,depth + 1);
    if(Node.NextSibling != None):
        ListOfTree(Node.NextSibling,depth);


# 后续
def ListOfTree2(Node:TreeNode,depth:int):
    empty = "  "
    if(Node.FirstChild != None):
        ListOfTree2(Node.FirstChild,depth + 1);
    if (Node.NextSibling != None):
        ListOfTree2(Node.NextSibling, depth);
    if(Node.Value == Node):
        print(empty*depth + "N")
    else:
        print(empty*depth + str(Node.Value))





N = TreeNode(0);
N.FirstChild = TreeNode(1)
N.FirstChild.FirstChild = TreeNode(2)
N.FirstChild.NextSibling = TreeNode(3)
N.FirstChild.NextSibling.FirstChild = TreeNode(7)
N.FirstChild.FirstChild.NextSibling = TreeNode(4)
N.FirstChild.FirstChild.NextSibling.NextSibling = TreeNode(5)
N.FirstChild.FirstChild.NextSibling.NextSibling.FirstChild = TreeNode(6)
ForeachTree(N)