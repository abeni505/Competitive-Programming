class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:

        for i in range(len(heights)):

            key=heights[i]
            key_name=names[i]
            j=i-1
            
            while j>=0 and heights[j]<key:
                heights[j+1]=heights[j]
                names[j+1]=names[j]

                heights[j]=key
                names[j]=key_name
                j-=1

        return names







      