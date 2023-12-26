class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        
        
        range_arr = [0]*(max(heights) + 1)

        hashmap = {}
        for i in range(len(heights)):
            hashmap[heights[i]] = names[i]

        for i in heights:
            range_arr[i] += 1
       

        new_names = []
        for i in range(len(range_arr) - 1, -1, -1):
            for j in range(range_arr[i]):
                new_names.append(hashmap[i])

        return new_names






