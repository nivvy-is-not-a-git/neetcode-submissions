# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        queue = deque()
        queue.append([root, [float('-inf'), float('inf')]])
        while queue:
            node, range = queue.popleft()
            

            if node.left:
                if node.left.val<=range[0] or node.left.val>=node.val:
                    return False
                package = [range[0], node.val]
                queue.append([node.left, package ])
                
            if node.right:
                if node.right.val<=node.val or node.right.val>=range[1]:
                    return False
                
                package = [node.val, range[1]]
                queue.append([node.right, package])
        return True
                
                
            
            
