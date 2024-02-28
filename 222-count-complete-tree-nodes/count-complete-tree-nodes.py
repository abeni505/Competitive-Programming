# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:

        if not root: return 0 
        
        queue = deque([root])

        ans = 0
        while queue:
            ans += 1 
            
            last_poped = queue.popleft()

            if last_poped.left:
                queue.append(last_poped.left)
            if last_poped.right:
                queue.append(last_poped.right)

        return ans

