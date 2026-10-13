# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(val = None, next = head)
        right = head
        left = dummy
        while n>1:
            n-=1
            right=right.next
        print (right.val)
        while right.next:
            left = left.next
            right=right.next
      
        left.next = left.next.next
        return dummy.next

            

        
        
