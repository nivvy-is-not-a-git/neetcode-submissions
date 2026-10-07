# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        queue = deque()
        queue.append([root, 0])
        levels = []
        while queue:
            
            node, height = queue.popleft()
            if not node:
                continue
            if len(levels)==height:
                levels.append([])
            levels[height].append(node.val)


            if node.left:
                queue.append([node.left, height+1])
                
                
            if node.right:
                queue.append([node.right, height+1])
              
        return levels
            
            
            
            
            
