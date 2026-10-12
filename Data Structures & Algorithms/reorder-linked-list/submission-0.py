# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        curr = head.next
        nodes = []
        while curr:
            nodes.append(curr)
            curr=curr.next
        left = 0
        right = len(nodes)-1
        curr = head
        while left<=right:
            curr.next = nodes[right]
            right -=1
            curr = curr.next
            curr.next = nodes[left]
            left +=1
            curr = curr.next
        curr.next = None
        return
        

            

            


            

            
        
    
        
        
