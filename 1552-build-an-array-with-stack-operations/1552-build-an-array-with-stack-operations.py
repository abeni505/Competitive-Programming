from typing import List

class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        new_arr = [i for i in range(1, n + 1)]
        output = []

        left = 0
        right = 0

        while right < len(target) and left < len(new_arr):

            if new_arr[left] == target[right]:
                output.append("Push")
                left += 1
                right += 1
            else:
                output.append("Push")
                output.append("Pop")
                left += 1

        return output
