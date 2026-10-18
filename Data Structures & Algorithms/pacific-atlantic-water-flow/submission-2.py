class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        def bfs(queue, visited):
            directions = [(-1, 0), (1,0), (0,1), (0,-1)]
            while queue:
                r, c = queue.popleft()
                
                for dc, dr in directions:
                    nr, nc = r+dr, c+dc
                    if nc < 0 or nc >= len(heights[0]) or nr<0 or nr>=len(heights):
                        continue
                    if (nr,nc) in visited:
                        continue
                    
                    if (heights[nr][nc]<heights[r][c]):
                        continue
                    visited.add((nr, nc))
                    queue.append((nr, nc))
                
            return visited
        atlantic_edges = deque()
        pacific_edges = deque()
        atlantic_visited = set()
        pacific_visited = set()
        
        for i in range(len(heights)):
            pacific_edges.append((i, 0))
            pacific_visited.add((i, 0))
            atlantic_edges.append((i, len(heights[0])-1))
            atlantic_visited.add((i, len(heights[0])-1))
        for i in range(len(heights[0])):
            pacific_edges.append((0, i))
            pacific_visited.add((0, i))
            atlantic_edges.append((len(heights)-1, i))
            atlantic_visited.add((len(heights)-1, i))
        atlantic_reachable = bfs(atlantic_edges,atlantic_visited)
        pacific_reachable = bfs(pacific_edges, pacific_visited)
        
        return list(atlantic_reachable & pacific_reachable)
        
        