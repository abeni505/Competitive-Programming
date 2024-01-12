class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        k = len(s1)
        left = 0
        check = defaultdict(int)

        count = Counter(s1)

        for right in range(len(s2)):
            check[s2[right]] += 1

            while right - left + 1 > k:
                check[s2[left]] -= 1
               
                if check[s2[left]] == 0:
                    del check[s2[left]]
                left += 1
         
            if check == count:
                return True

        return False






