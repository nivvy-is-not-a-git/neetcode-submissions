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
        nodes_list = []
        nodes_hash = {} #Node: index
        curr = head
        i = 0
        while curr:
            nodes_hash[curr] = i
            nodes_list.append(Node(curr.val))
            i+=1
            curr = curr.next
        curr = head
        for i, node in enumerate(nodes_list):
            if curr.random:
                node.random = nodes_list[nodes_hash[curr.random]]
            if i<len(nodes_list)-1:
                node.next = nodes_list[i+1]
            curr = curr.next
        return nodes_list[0] if nodes_list else None
        

        