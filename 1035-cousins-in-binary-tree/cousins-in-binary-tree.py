# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:
        

        queue = deque([(root, 0)])
        parent = {root.val : (-1, 0)}

        while queue:

            for _ in range(len(queue)):

                node , level = queue.popleft()

                if node.left:
                    if node.left.val not in parent:
                        queue.append((node.left , level + 1))
                        parent[node.left.val] = (node.val , level + 1)
                if node.right:
                    if node.right.val not in parent:

                        parent[node.right.val] = (node.val , level + 1)
                        queue.append((node.right , level + 1))
        
        if parent[x][1] == parent[y][1] and parent[x][0] != parent[y][0]:
            return True
        return False



