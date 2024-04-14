# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        
        output = []

       
        queue = deque([root])
        sum_left = 0
        while queue:

            curr = queue.popleft()

            if curr.left:
                if not curr.left.left and not curr.left.right:
                    sum_left += curr.left.val
                else:
                    queue.append(curr.left)

            if curr.right:
                queue.append(curr.right)

        
        return sum_left