class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        
        stack = []
        hashset = set()
        count = Counter(s)

        for i in range(len(s)):
    
            while stack and stack[-1] > s[i] and count[stack[-1]] > 0 and s[i] not in hashset:
                hashset.discard(stack.pop())

            if s[i] not in hashset:
                stack.append(s[i])
                hashset.add(s[i])
            count[s[i]] -= 1

        return "".join(stack)
