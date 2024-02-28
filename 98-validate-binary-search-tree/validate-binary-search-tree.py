# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        inorder = []
        def inorder_t (root):
            if not root:
                return

            inorder_t(root.left)
            inorder.append(root.val)
            inorder_t(root.right)

        inorder_t(root)
        return inorder == sorted(inorder) and len(inorder) == len(set(inorder))
