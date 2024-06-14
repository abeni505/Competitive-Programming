class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        hashmap = defaultdict(list)

        for i in range(len(strs)):
            count = sorted(strs[i])
            hashmap[tuple(count)].append(i)
            
        
        output = []
        for key , val in hashmap.items():
            curr  = []
            for j in val:
                curr.append(strs[j])
            
            output.append(curr)
            
        return output