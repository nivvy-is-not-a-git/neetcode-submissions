class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def backtrack(x, y, current_index):
            nonlocal word_spotted
            nonlocal current_word
            if x>=len(board[0]) or x<0:
                return
            if y>=len(board) or y<0:
                return
            if (x, y) in visited:
                return
            if word_spotted == True:
                return 
            current_word += board[y][x]
            visited.add((x, y))
            if current_word[-1] != word[current_index]:
                visited.remove((x, y))
                current_word = current_word[:-1]
                return 
            if current_word == word:
                word_spotted = True
                return 
            
            
            backtrack(x+1, y, current_index+1)
            backtrack(x, y+1, current_index+1)
            backtrack(x-1, y, current_index+1)
            backtrack(x, y-1, current_index+1)
            current_word = current_word[:-1]
            visited.remove((x, y))

        current_word = ""
        word_spotted = False
        visited = set()
        for i in range(len(board)):
            for j in range(len(board[i])):
                backtrack(j, i, 0)
        return word_spotted
