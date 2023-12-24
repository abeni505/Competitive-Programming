#User function Template for python3


class Solution:
    
    #Function to rotate matrix anticlockwise by 90 degrees.
    def rotateby90(self,a, n): 
        # code here
        for r in range(n):
            for c in range(n//2):
                matrix[r][c] , matrix[r][n - 1 - c] = matrix[r][n -1 - c] , matrix[r][c] 
        
        for row in range(n):
            for col in range(row + 1):
                matrix[row][col] , matrix[col][row] = matrix[col][row], matrix[row][col]
                
                

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        n = int(input())
        matrix = [[0 for j in range(n)] for i in range(n)]
        line1 = [int(x) for x in input().strip().split()]
        k=0
        for i in range(n):
            for j in range (n):
                matrix[i][j]=line1[k]
                k+=1
        obj = Solution()
        obj.rotateby90(matrix,n)
        for i in range(n):
            for j in range(n):
                print(matrix[i][j],end=" ")
        print()

# } Driver Code Ends