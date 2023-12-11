class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:

        count = Counter(arr)

        operation = len(arr) * 25/100

        for key , val in count.items():
            if val > operation:
                return key