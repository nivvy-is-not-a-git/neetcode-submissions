class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        def dfs(root, visiting):
            if root in visiting:
                return
            visiting.add(root)
            for neighbour in adjacency[root]:
                dfs(neighbour, visiting)
            return
        
        if len(edges)!=n-1:
            return False
        adjacency = [[] for _ in range(n)]
        for node, neighbour in edges:
            adjacency[node].append(neighbour)
            adjacency[neighbour].append(node)
        visiting = set()
        dfs(0, visiting)
        return len(visiting)==n
        
        
            
            
        
