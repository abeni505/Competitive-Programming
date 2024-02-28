# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        
        queue = deque([root])

        while queue:
            last_poped = queue.popleft()
            if last_poped.right:
                queue.append(last_poped.right)
            if last_poped.left:
                queue.append(last_poped.left)
            
        return last_poped.val