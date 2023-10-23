class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = [(position[i], speed[i]) for i in range(len(position))]
        cars.sort(reverse=True)
        stack = []

        for i in range(len(cars)):
            p, s = cars[i]
            t = (target - p) / s

            if not stack:
                stack.append(t)
            else:
                if t > stack[-1]:
                    stack.append(t)

        return len(stack)
