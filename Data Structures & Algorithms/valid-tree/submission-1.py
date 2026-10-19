class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        def dfs(root, visiting, past_node):
            if root in visiting:
                return False
            if root in visited:
                return True
            visiting.add(root)
            for neighbour in adjacency[root]:
                if past_node!=neighbour:
                    if not dfs(neighbour, visiting, root):
                        return False
            visited.add(root)
            visiting.remove(root)
            return True
        adjacency = {}
        for i in range(n):
            adjacency[i] = set()
        for node, neighbour in edges:
            adjacency[node].add(neighbour)
            adjacency[neighbour].add(node)
        
        visited = set()
        if not dfs(0, set(), None) or len(visited)<n:
            return False
        return True
        
        
            
            
        
