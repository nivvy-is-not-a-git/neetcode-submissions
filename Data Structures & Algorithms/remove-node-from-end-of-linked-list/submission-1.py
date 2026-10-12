# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        curr = head
        size = 0
        while curr:
            curr=curr.next
            size+=1
        curr = head
        print(size)
        new_index = size - n
        prev = None
        while new_index>0:
            prev = curr
            curr=curr.next
            new_index-=1
        if prev is None:
            return curr.next
        prev.next = curr.next
        return head

            

        
        
