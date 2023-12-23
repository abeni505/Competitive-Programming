class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:


        def binarysort(nums):
            left = 0
            right = len(nums) - 1

            while left <= right:

                mid = (left + right)// 2

                if nums[mid] == 1:
                    left = mid + 1
                
                else:
                    right = mid - 1

            return left

        hashmap = defaultdict(int)
        for row in range(len(mat)):
            hashmap[row] = binarysort(mat[row])

     
        hashmap_sorted = sorted(hashmap.items() , key = lambda x: x[1])

        ans = []
        for key , value in hashmap_sorted:
            ans.append(key)
        
        return ans[:k]



        