#User function Template for python3

class Solution: 
    def select(self, arr, i):
        # code here 
        min_index=i
        for x in range(i+1,len(arr)):
            if arr[x]<arr[min_index]:
                min_index=x
        
        return min_index
            
    
    def selectionSort(self, arr,n):
        #code here
        for z in range(n):
            minimum=self.select(arr,z)
            arr[z],arr[minimum]=arr[minimum],arr[z]
        
        return arr


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int(input())
    for _ in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        Solution().selectionSort(arr, n)
        for i in range(n):
            print(arr[i],end=" ")
        print()
# } Driver Code Ends