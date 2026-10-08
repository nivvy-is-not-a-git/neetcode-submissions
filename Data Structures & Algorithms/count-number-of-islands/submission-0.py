from collections import deque
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visited = set()
        islands = 0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j]=="0" or (i, j) in visited:
                    continue
                else:
                    
                    queue = deque()
                    queue.append((i, j))
                    visited.add((i, j))
                    while queue:
                        coords = queue.popleft()
                        down = (coords[0]+1, coords[1])
                        up = (coords[0]-1, coords[1])
                        right = (coords[0], coords[1]+1)
                        left = (coords[0], coords[1]-1)
                        
                        if coords[0]!=len(grid)-1 and grid[down[0]][down[1]] == "1" and down not in visited:
                            queue.append(down)
                            visited.add(down)
                        if coords[0]!=0 and grid[up[0]][up[1]]=="1" and up not in visited:
                            queue.append(up)
                            visited.add(up)
                        if coords[1]!=len(grid[0])-1 and grid[right[0]][right[1]] == "1" and right not in visited:
                            queue.append(right)
                            visited.add(right)
                        if coords[1]!=0 and grid[left[0]][left[1]] == "1" and left not in visited:
                            queue.append(left)
                            visited.add(left)
                    islands+=1
        print(len(visited))
        return islands

                

    

        

