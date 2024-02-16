class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        count = Counter(arr)

        count_arr = sorted(count.items() , key = lambda x:x[1])
       

        for key , val in count_arr:
            if val <= k:
                k -= val
                del count[key]
            else:
                break

        return len(count)