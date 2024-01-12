class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        
        left = count_v = max_ = 0
        vowels = {'a', 'e', 'i', 'o' , 'u'}
        count = deque()
        

        for right in range(len(s)):

            if s[right] in vowels:
                count_v += 1
            count.append(s[right])
            while len(count) > k:
                if s[left] in vowels:
                    count_v -= 1
                count.popleft()
                left+= 1

            max_ = max(max_ , count_v)

        return max_