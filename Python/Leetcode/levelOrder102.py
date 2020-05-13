# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        l = []
        if root.val == None:
            return l
        l.append([root])
        while(len(l[-1]) != 0):
                l.append(self.leafs(l[-1]))
        del l[-1]
        return l

    def leafs(self,roots) -> List[TreeNode]:
        t = []
        for i in range(len(roots)):
            if roots[i] == None:
                t.append(None)
                t.append(None)
            else:
                t.append(roots[i].left)
                t.append(roots[i].right)

        return t