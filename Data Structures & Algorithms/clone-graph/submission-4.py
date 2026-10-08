"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""
from collections import deque
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
       

        queue = deque()
        queue.append(node)
        if node is None:
            return
        visited = {}
        while queue:
            old_node = queue.popleft()
            new_adjacency = []
            for neighbour in old_node.neighbors:
                if neighbour not in visited:
                    neighbour_node = Node(neighbour.val)
                    visited[neighbour] = neighbour_node
                    queue.append(neighbour)
                    new_adjacency.append(visited[neighbour])

                else:
                    new_adjacency.append(visited[neighbour])
            if old_node not in visited:
                new_node = Node(old_node.val, new_adjacency)
                visited[node] = new_node
            else:
                visited[old_node].neighbors = new_adjacency
        return visited[node]



                    
        

