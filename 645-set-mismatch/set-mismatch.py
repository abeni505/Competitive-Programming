class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:

        output = []

        count = Counter(nums)
        for key ,val in count.items():
            if val == 2:
                output.append(key)

        for i in range(len(nums)):
            if i+1 not in count:
                output.append(i + 1)

        return output