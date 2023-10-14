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

        for j in range(len(counter)-1,-1,-1):
            for k in range(counter[j]):
                sorted_arr.append(hashmap[j])

        return sorted_arr




      