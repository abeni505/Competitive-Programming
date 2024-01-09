# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        def leaf(root , arr):
            if not root:
                return 0
            
            if root.left == None and root.right == None:
                arr.append(root.val)
            
            leaf(root.left,arr)
            leaf(root.right,arr)

        arr1 = []
        arr2 = []
        leaf(root1,arr1)
        leaf(root2,arr2)
       
        return arr1 == arr2