class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        left=0
        summ=0
        count=0
        for right in range(len(arr)):

            summ+=arr[right]

            if right - left==k-1:
                avg=summ/k
                if avg >= threshold:
                    count+=1
                summ-=arr[left]
                left+=1
                
                
        return count
