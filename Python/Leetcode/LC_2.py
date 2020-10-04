# 给出两个 非空 的链表用来表示两个非负的整数。其中，它们各自的位数是按照 逆序 的方式存储的，并且它们的每个节点只能存储 一位 数字。
# 如果，我们将这两个数相加起来，则会返回一个新的链表来表示它们的和。
# 您可以假设除了数字 0 之外，这两个数都不会以 0 开头。
# 示例：
# 输入：(2 -> 4 -> 3) + (5 -> 6 -> 4)
# 输出：7 -> 0 -> 8
# 原因：342 + 465 = 807

import math;
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        bit = 0;
        List = None;
        while(l1 != None or l2 != None):
            if(List == None):
                List = ListNode(0);
                Head = List;
            else:
                List.next = ListNode(0);
                List = List.next;
            a1 = 0
            a2 = 0
            if(l1 != None):
                a1 = l1.val;
                l1 = l1.next
            if(l2 != None):
                a2 = l2.val;
                l2 = l2.next;
            value = a1 + a2 + bit;
            bit = math.floor(value/10)%10
            value = value%10;
            List.val = value;
            if(bit > 0):
                List.next = ListNode(bit);

        return Head
