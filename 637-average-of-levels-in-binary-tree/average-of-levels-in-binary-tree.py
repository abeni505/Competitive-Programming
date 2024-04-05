# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        
        queue = deque([root])

        output = []
        while queue:
            level = []

            for i in range(len(queue)):
                curr = queue.popleft()
                level.append(curr.val)
            
                if curr.left:
                    queue.append(curr.left)
                
                if curr.right:
                    queue.append(curr.right)
            output.append(sum(level)/len(level))

        return output
