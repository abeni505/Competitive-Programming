# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        
        count = 0
        def dfs (root):
            nonlocal count
            if not root: return

            count += 1
            dfs(root.left)
            dfs(root.right)
        

        def left_height(root , Left):
            height = 0
            while root:
                if Left:
                    root = root.left
                else:
                    root = root.right
                height += 1
            return height


        if left_height(root , True) == left_height(root,False):
            return 2**left_height(root,True) - 1
        else:
            dfs(root)
            return count

