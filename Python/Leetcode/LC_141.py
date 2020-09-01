# 给定一个链表，判断链表中是否有环。
#
# 为了表示给定链表中的环，我们使用整数 pos 来表示链表尾连接到链表中的位置（索引从 0 开始）。 如果 pos 是 -1，则在该链表中没有环。

# 解题思路：快慢指针 如果成环，快慢指针终会相遇
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        if (head == None or head.next == None):
            return False;
        slow,fast = head,head.next
        while(fast != None and fast.next != None):
            if(slow == fast):
                return True;
            slow = slow.next
            fast = fast.next.next
        return False;