class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        longest_sub=0
        window=set()
        left=0


        for right in range(len(s)):

            if s[right] not in window:
                window.add(s[right])
            else:
                while s[right] in window:
                    window.remove(s[left])
                    left+=1
                window.add(s[right])
            
            longest_sub=max(longest_sub,right-left+1)

        return longest_sub            


            
                    
        
