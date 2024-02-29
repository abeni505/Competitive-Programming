# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        if not root: return
        queue = deque([root])
        output = []

        flag = True
        while queue:
    
            level = []
            for i in range(len(queue)):
                last_poped = queue.popleft()
                level.append(last_poped.val)
            
                if last_poped.left:
                    queue.append(last_poped.left)
                if last_poped.right:
                    queue.append(last_poped.right)

            if flag:
                output.append(level)
                flag = False
            else:
                output.append(level[::-1])
                flag = True
           
        

        return output
