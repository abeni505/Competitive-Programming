class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:
        def recur(left, right):
            if left == right:
                return nums[left]
            leftchoice = nums[left] - recur(left+1, right)
            rightchoice = nums[right] - recur(left, right-1)

            return max(leftchoice, rightchoice)
               
        result = recur(0, len(nums) - 1)
        return result >= 0
