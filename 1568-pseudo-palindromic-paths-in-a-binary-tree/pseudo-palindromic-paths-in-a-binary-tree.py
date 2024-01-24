# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pseudoPalindromicPaths (self, root: Optional[TreeNode]) -> int:
        
        count = Counter()
        Total = 0
        def dfs(root):
            nonlocal Total

            if not root:
                return

            count[root.val] += 1
            if not root.left and not root.right:
                c = 0
                for val in count.values():
                    if val & 1:
                        c += 1
                if c <= 1:
                    Total += 1
                       
                

            dfs(root.left)
            dfs(root.right)
            count[root.val] -= 1

        dfs(root)
        return Total