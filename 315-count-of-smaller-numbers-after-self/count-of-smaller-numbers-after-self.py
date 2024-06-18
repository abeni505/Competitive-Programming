class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        lookup = defaultdict
        idx = [i for i in range(len(nums))]
        ans = [0] * len(nums)

        def conquer(left, right):
            i = j = 0
            merged = []
            while i < len(left) or j < len(right):
                if j >= len(right) or (i < len(left) and nums[left[i]] <= nums[right[j]]):
                    merged.append(left[i])
                    ans[left[i]] += j
                    i += 1
                else:
                    merged.append(right[j])
                    j += 1

            return merged


        def divide(idx):
            if not idx:
                return
            if len(idx) == 1:
                return idx

            mid = len(idx) // 2
            left = divide(idx[:mid])
            right = divide(idx[mid:])
            
            return conquer(left, right)


        divide(idx)
        return ans
