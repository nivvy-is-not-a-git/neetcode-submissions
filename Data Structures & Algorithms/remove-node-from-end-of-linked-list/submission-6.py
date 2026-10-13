# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        right = head
        left = head
        while n>1:
            n-=1
            right=right.next
        prev = None

        while right.next:
            prev = left
            left = left.next
            right=right.next
        print (left.val, right.val)
        if prev is None:
            return head.next
        prev.next = left.next
        return head

            

        
        
