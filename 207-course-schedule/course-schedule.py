class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adjlst = defaultdict(list)

        for c1 , c2 in prerequisites:
            adjlst[c2].append(c1)

        state = [0] * numCourses

    
        # Each vertex can have 3 different states:
        # state 0   : vertex is not visited. It's a default state.
        # state -1  : vertex is being processed. Either all of its descendants
        #             are not processed or it's still in the function call stack.
        # state 1   : vertex and all its descendants are processed.
    
        def hasCycle(v):
            if state[v] == 1:
                # This vertex is processed so we pass.
                return False
            if state[v] == -1:
                # This vertex is being processed and it means we have a cycle.
                return True

            # Set state to -1
            state[v] = -1

            for i in adjlst[v]:
                if hasCycle(i):
                    return True

            state[v] = 1
            return False

        # we traverse each vertex using DFS, if we find a cycle, stop and return
        for v in range(numCourses):
            if hasCycle(v):
                return False

        return True