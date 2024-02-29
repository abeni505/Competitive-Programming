# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isEvenOddTree(self, root: Optional[TreeNode]) -> bool:
        
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
            output.append(level)

            if len(level) != len(set(level)):
                return False
            if flag:
                flag = False
                if level != sorted(level) or any(i % 2 == 0 for i in level):
                    return False
                
                
            else:
                flag = True
                # print(level[::-1] , sorted(level))
                if level[::-1] != sorted(level) or any(i % 2 == 1 for i in level):
                    return False
        # print(output)
        return True



