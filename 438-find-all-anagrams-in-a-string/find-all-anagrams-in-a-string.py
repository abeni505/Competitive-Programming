class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        
        k = len(p)
        countp = Counter(p)

        check = deque()
        output = []
        left = right = 0
        while right < len(s):
            if right - left <= k:
                check.append(s[right])
                right += 1
                # print(check)
                if  right - left == k:
                    counts = Counter(check)
                    check.popleft()
                    left += 1
                    if counts == countp:
                        output.append(right - k)
        
        return output
