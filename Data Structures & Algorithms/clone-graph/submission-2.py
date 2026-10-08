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
        graph = []
        queue = deque()
        if node is None:
            return 
        queue.append(node)
        
        visited = {}
        
        while queue:
            popped_node = queue.popleft()
            
            new_adjacency = []
            for neighbour in popped_node.neighbors:
                if neighbour not in visited:
                    new_neighbour = Node(neighbour.val)
                    queue.append(neighbour)
                    visited[neighbour] = new_neighbour
                    new_adjacency.append(new_neighbour)
                else:
                    new_adjacency.append(visited[neighbour])

            if popped_node not in visited:
                new_node = Node(popped_node.val, new_adjacency)
                visited[popped_node] = new_node
            else:
                visited[popped_node].neighbors = new_adjacency

        return visited[node]
        





