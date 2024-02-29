# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        level_order = defaultdict(list)
        def dfs(root,level,depth):
            if not root:
                return
            level_order[level].append((depth,root.val))
            dfs(root.left,level -1 ,depth + 1)
            dfs(root.right,level + 1 , depth + 1)
        

        dfs(root,0,0)

        keys = sorted(level_order.keys())

       
        output = []
        for key in keys:
            level_order[key].sort()
            
            output = []
            for depth , val in level_order[key]:
                output.append(val)

            yield output