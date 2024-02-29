# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        
        output = []
        ans = 0
        def dfs(root):
            nonlocal ans
            if not root: return 

            output.append(str(root.val))
            dfs(root.left) 
            dfs(root.right)

            if not root.left and not root.right:

                ans += int("".join(output))
                print(output , ans)
                output.pop()
                return
            
            if output and output[-1] == str(root.val):
                output.pop() 

        dfs(root)
        
        return ans