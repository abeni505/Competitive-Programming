# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        
        upper  = [root]
        lower = []

        while True:
            for i in upper:
                if i.left:
                    lower.append(i.left)
                if i.right:
                    lower.append(i.right)
            if not lower:
                return upper[0].val
            upper = lower.copy()
            lower = []
