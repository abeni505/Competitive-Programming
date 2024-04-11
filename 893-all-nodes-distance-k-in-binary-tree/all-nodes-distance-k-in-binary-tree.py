# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        
        adjlist = defaultdict(list)

        curr = root
        def addtoadj(curr):
            if curr.left:
                adjlist[curr.val].append(curr.left.val)
                adjlist[curr.left.val].append(curr.val)

            if curr.right:
                adjlist[curr.val].append(curr.right.val)
                adjlist[curr.right.val].append(curr.val)

        def dfs(root):
            if not root:return

            addtoadj(root)

            if root.left:
                dfs(root.left)
            if root.right:
                dfs(root.right)

        dfs(root)
    

        queue = deque([(target.val)])
        visited = set([(target.val)])
        dist = 0
        while queue:
         
            if dist == k:
                return list(queue)

            for _ in range(len(queue)):
                
                node = queue.popleft()

                for nbr in adjlist[node]:
                    if nbr not in visited:
                        queue.append(nbr)
                        visited.add(nbr)
            dist += 1

        return []

            

