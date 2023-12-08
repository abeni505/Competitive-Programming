# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:

        cur = str(root.val)
        r = ''
        l = ''

        if root.right:
            r = "(" + self.tree2str(root.right) + ')'
        if root.left:
            l = "(" + self.tree2str(root.left) + ')'
        elif root.right:
            l = "()"
        
        return cur + l + r
