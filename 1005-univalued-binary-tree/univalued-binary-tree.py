# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isUnivalTree(self, root: Optional[TreeNode]) -> bool:
        
        queue = deque([root])
      
        level = set()
        while queue:

            for i in range(len(queue)):
                curr = queue.popleft()
                level.add(curr.val)
            
                if curr.left:
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)
            if len(level) != 1:
                return False
        return True
            
            