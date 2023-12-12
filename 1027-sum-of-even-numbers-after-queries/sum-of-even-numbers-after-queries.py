class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:

        # def check_evensum(nums):
        #     even_sum = 0
        #     for i in nums:
        #         if i % 2 == 0:
        #             even_sum += 1
        #     return even_sum
        even_sum = sum(x for x in nums if x % 2 == 0)
       
        out_put = []
        for val , index in queries:
        
            if nums[index] % 2 == 0 :
                even_sum -= nums[index]
                
            nums[index] = nums[index] + val

            if nums[index] % 2 == 0:
                even_sum += nums[index]
            out_put.append(even_sum)

        return out_put






        

        # i = 0
        # even_sum = 0
        # for num in nums:
        #     if num % 2 == 0:
        #         even_sum += num

        # out_put = []
        # while i < len(nums):
        #     if i in hashmap:
        #         nums[i] += hashmap[i]
        #         if nums[i] % 2 == 0:
        #             even_sum += nums[i]
        #         out_put.append(even_sum)
        #     i += 1
        # return out_put

            

