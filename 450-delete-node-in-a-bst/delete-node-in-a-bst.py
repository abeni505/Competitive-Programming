# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        

        def helper(root):
            curr = root
            while curr.left:
                curr = curr.left
            
            return curr

        def delete(root , key):
            if not root:
                return 
            if root.val == key:
                if root.left and root.right:

                    temp = helper(root.right)
                    root.val = temp.val

                    root.right = delete(root.right , temp.val)
                
                elif (not root.left and root.right):
                    return root.right
                elif not root.right and root.left:
                    return root.left
                else:
                    return None

            
            elif root.val < key:
                root.right = delete(root.right , key)
            else:
                root.left = delete(root.left , key)

            return root

        return delete(root , key)