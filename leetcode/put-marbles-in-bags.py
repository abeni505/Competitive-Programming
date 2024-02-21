class Solution:
    def putMarbles(self, weights: List[int], k: int) -> int:

        new = []
        for i in range(1,len(weights)):
            new.append(weights[i] + weights[i - 1])
        
        new = sorted(new , reverse = True)
        max_diff = 0
        print(new)

        left = 0
        right = len(new) - 1
        while (k - 1):
            max_diff += new[left] - new[right]
            left += 1
            right -= 1
            
            k-=1
        
        return max_diff
        