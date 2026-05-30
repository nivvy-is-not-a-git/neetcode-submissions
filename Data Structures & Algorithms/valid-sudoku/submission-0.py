class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        columnmap = []
        rowmap = []
        boxmap={}
        for i in range(9):
            columnmap.append({})
            rowmap.append({})

        for i in range(9):
            

            for j in range(9):
            
                if (i//3, j//3) not in boxmap:
                    boxmap[(i//3, j//3)] = {}
                if board[i][j] == ".":
                    continue
                if board[i][j] in rowmap[i] or board[i][j] in columnmap[j] or board[i][j] in boxmap[(i//3, j//3)]:
                    
                    print ("index", i, j)
                    print (board[i][j])
                    return False
                else:
                    rowmap[i][board[i][j]]= 1
                    columnmap[j][board[i][j]]= 1
                
                    
                    boxmap[i//3, j//3][board[i][j]] = 1
        return True
                
        
                 



                