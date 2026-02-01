1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) 
-> Optional[ListNode]:
        slow = head
        fast = head
        while n > 0 :
            fast = fast.next
            n -= 1

        while fast and fast.next:
            fast = fast.next
            slow = slow.next
        # print(slow)

        if fast:
            slow.next = slow.next.next