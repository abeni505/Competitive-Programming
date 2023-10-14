class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        hashmap={}
        sorted_arr=[]
        for x in range(len(heights)):
            hashmap[heights[x]]=names[x]

        for i in range(len(heights)):

            max_index=i

            for j in range(i+1,len(heights)):
                if heights[j]>heights[max_index]:
                    max_index=j
            
            heights[i],heights[max_index]=heights[max_index],heights[i]

        for k in heights:
            sorted_arr.append(hashmap[k])




        return sorted_arr


        







      