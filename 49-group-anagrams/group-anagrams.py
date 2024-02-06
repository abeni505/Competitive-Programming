class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap=defaultdict(list)
        for s in strs:
            count =[0]*26

            for char in s:
                count[ord(char)-ord("a")]+=1

            hashmap[tuple(count)].append(s)
 
        return list(hashmap.values())
