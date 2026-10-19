class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        def dfs(root, visited):
            if root in visited:
                return
            visited.add(root)
            for neighbour in adjacency[root]:
                dfs(neighbour, visited)
        if len(edges)!=n-1:
            return False
        adjacency = [[] for _ in range(n)]
        for node, neighbour in edges:
            adjacency[node].append(neighbour)
            adjacency[neighbour].append(node)
        visited = set()
        dfs(0, visited)
        return len(visited)==n
        
        
            
            
        
