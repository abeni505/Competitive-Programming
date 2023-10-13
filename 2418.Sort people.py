class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        pair={}
        arr=[]
        for j in range(len(names)):
            pair[heights[j]]=names[j]

        for i in range(len(heights)):
            for j in range(len(heights)-1-i):
                if heights[j]<heights[j+1]:
                    heights[j],heights[j+1]=heights[j+1],heights[j]
        for k in heights:
            arr.append(pair[k])
        
        return arr

        
        
