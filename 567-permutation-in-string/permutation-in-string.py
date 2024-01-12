class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        k = len(s1)
        left = 0
        window = deque(s2[:k])

        count = Counter(s1)

        for i in range(k):
            if Counter(window) == count:
                return True
        
        for right in range(k , len(s2)):
            window.popleft()
            left += 1
            window.append(s2[right])
            if Counter(window) == count:
                return True
        
        return False





