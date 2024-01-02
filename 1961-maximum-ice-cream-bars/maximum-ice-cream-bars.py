class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        
        counter = [0] * (max(costs) + 1)

        for i in costs:
            counter[i] += 1

        new_nums = []
        for j in range(len(counter)):
            for k in range(counter[j]):
                new_nums.append(j)

        cur_sum = 0
        max_ = 0
        for k in range(len(new_nums)):
            
            coins -= new_nums[k]
            if coins < 0:
                break
            max_ = k + 1

        return max_
