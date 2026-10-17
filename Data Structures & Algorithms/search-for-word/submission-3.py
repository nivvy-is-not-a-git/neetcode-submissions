class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def backtrack(x, y, current_index):
            nonlocal word_spotted
            if x>=len(board[0]) or x<0:
                return False
            if y>=len(board) or y<0:
                return False
            if (x, y) in visited:
                return False
            if board[y][x] != word[current_index]:
                return False
            if current_index == len(word)-1:
                return True
            
            visited.add((x, y))
            found = (backtrack(x+1, y, current_index+1) or backtrack(x, y+1, current_index+1) 
            or backtrack(x-1, y, current_index+1) or backtrack(x, y-1, current_index+1))
            visited.remove((x, y))
            return found

        word_spotted = False
        visited = set()
        for i in range(len(board)):
            for j in range(len(board[i])):
                if backtrack(j, i, 0):
                    return True
        return False
