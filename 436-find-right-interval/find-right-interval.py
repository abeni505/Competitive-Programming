class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        
        hashmap = defaultdict(lambda : -1)
        i = 0
        for a , b in intervals:
            hashmap[a] = i
            i += 1
        
        new = sorted(intervals , key = lambda x: x[0])
        new = [a for a , b in new]
        
        output = []
        for a , b in intervals:
            indx = bisect_left(new, b)
     
            if indx >= len(new):
                val = "notvalid"
            else:
                val = new[indx]
            output.append(hashmap[val])
            
        return output