class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        

        hashmap={}

        for x in range(len(heights)):
            hashmap[heights[x]]=names[x]

        h=max(heights)+1
        counter=[0]*h
        sorted_arr=[]
        for i in heights:
            counter[i]+=1
            
        target=0
        for index,value in enumerate(counter):
            for j in range(value):
                heights[target]=index
                target+=1

        for y in reversed(heights):
            sorted_arr.append(hashmap[y])

        return sorted_arr




      