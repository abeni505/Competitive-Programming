# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        output = []
        if not root: return

        upper = [root]
        lower = []
    
        flag = False
        while True:
            
            curr = []
            for i in upper:
                if i.left:
                    lower.append(i.left)
                if i.right:
                    lower.append(i.right)

                curr.append(i.val)
                
            if not flag:
                output.append(curr)
                flag = True
            else:
                output.append(curr[::-1])
                flag = False


            if not lower:
                return output
            upper = lower.copy()
            lower = []
   
            