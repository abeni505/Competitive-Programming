class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:


        hashmap={}
        sorted_arr=[]
        for x in range(len(heights)):
            hashmap[heights[x]]=names[x]


        for i in range(len(heights)):

            key=heights[i]
            j=i-1
            
            while j>=0 and heights[j]<key:
                heights[j+1]=heights[j]
                heights[j]=key
                j-=1
        for k in heights:
            sorted_arr.append(hashmap[k])

        return sorted_arr







      