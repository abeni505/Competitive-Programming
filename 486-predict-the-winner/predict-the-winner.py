class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:
        def recur(turn, left, right):
            if left == right:
                if turn == 0:
                    return [nums[left], 0]
                return [0, nums[left]]

                
            leftchoice = recur(1-turn, left+1, right)
            leftchoice[turn] += nums[left]
            rightchoice = recur(1-turn, left, right-1)
            rightchoice[turn] += nums[right]

            leftdiff = leftchoice[0] - leftchoice[1]
            rightdiff = rightchoice[0] - rightchoice[1]
            if turn == 0:
                if leftdiff > rightdiff:
                    return leftchoice
                return rightchoice
            else:
                if leftdiff < rightdiff:
                    return leftchoice
                return rightchoice
               
        result = recur(0, 0, len(nums) - 1)
        return result[0] >= result[1]
