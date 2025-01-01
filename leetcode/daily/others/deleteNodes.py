from typing import List, Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def delNodes(self, root: Optional[TreeNode]) -> List[TreeNode]:
        nodes = {}
        
        for p, c, left in root:
            if p not in nodes:
                nodes[p] = TreeNode(p)
            if c not in nodes:
                nodes[c] = TreeNode(c)
            
            if left:
                nodes[p].left = nodes[c]
            else:
                nodes[p].right = nodes[c]
        
        root = None
        for p, _, _ in descriptions:
            if p not in nodes.values():
                root = nodes[p]
                break
        
        return root

# Exemplo de uso:
root_node = Solution().createBinaryTree([[20,15,1],[20,17,0],[50,20,1],[50,80,0],[80,19,1]])
