# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        if not root:return

        output = []
        level = []
        depth = 0

        queue = deque([(root,0)])
        while queue:
            node , nodedepth = queue.popleft()

            if not node:
                continue

            if nodedepth != depth:
                output.append(level[:])
                depth += 1
                level = []

            level.append(node.val)
            queue.append((node.left , depth + 1))
            queue.append((node.right , depth + 1))
        
        if level:
            output.append(level[:])

            
        return output



        