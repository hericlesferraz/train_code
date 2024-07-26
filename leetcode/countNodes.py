from typing import Optional
from collections import Counter

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
   

class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        return 1 + self.countNodes(root.left) + self.countNodes(root.right)
    
Solution().countNodes(root=[1,2,3,4,5])
    
