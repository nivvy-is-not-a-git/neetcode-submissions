# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        new = ListNode(val = None, next = None)
        new_curr = new
        curr1 = list1
        curr2 = list2

        while curr1 is not None or curr2 is not None:

            if curr2 is None:
                new_curr.next = curr1   
                curr1=curr1.next
            elif curr1 is None:
                new_curr.next = curr2
                curr2=curr2.next
            elif curr1.val<curr2.val:
                new_curr.next = curr1   
                curr1=curr1.next
            else:
                new_curr.next = curr2
                curr2=curr2.next
            
            new_curr = new_curr.next
        return new.next

        
            