class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:


        for i in range(len(heights)):
            max_index=i          
            for j in range(i+1,len(heights)):
                if heights[j]>heights[max_index]:
                    max_index=j
            heights[i],heights[max_index]=heights[max_index],heights[i]
            names[i],names[max_index]=names[max_index],names[i]

        return names
        

        

        
       


            