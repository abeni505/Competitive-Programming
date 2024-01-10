class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        
        k = len(p)
        output = []
    
        
        count_target = Counter(p)
        count_check = Counter(s[:k])

        if count_check == count_target:
                output.append(0)
        
        for i in range(k ,len(s)):
            cur_char = s[i]
            count_check[cur_char] += 1
            count_check[s[i - k]] -= 1

            if count_check == count_target:
                output.append(i - k + 1)

        
        return output



