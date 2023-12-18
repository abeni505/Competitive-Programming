class Solution:
    def maxProductDifference(self, nums: List[int]) -> int:
        
        largest , second_large = 0 , 0
        smallest , second_small = float('inf') , float('inf')

        for i in nums:
            if i > largest:
                second_large = largest
                largest = i
            elif i > second_large:
                second_large = i
            if i < smallest:
                second_small = smallest
                smallest = i
            elif i < second_small:
                second_small = i
        
        return (largest * second_large) - (smallest * second_small)