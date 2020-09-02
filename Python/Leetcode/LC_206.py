# 反转一个单链表。
# 你可以迭代或递归地反转链表。
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        p = head;
        prev = None;
        while(p != None):
            temp = p.next
            p.next = prev
            prev = p
            p = temp
        return prev