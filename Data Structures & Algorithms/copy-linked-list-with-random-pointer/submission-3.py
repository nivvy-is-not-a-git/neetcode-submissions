"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        nodes_hash = {} #Node: index
        curr = head
        while curr:
            nodes_hash[curr] = Node(curr.val)
            curr = curr.next
        curr = head
        while curr:
            if curr.random:
                nodes_hash[curr].random = nodes_hash[curr.random]
            if curr.next:
                nodes_hash[curr].next = nodes_hash[curr.next]
            curr = curr.next
        return nodes_hash[head] if head else None
        

        