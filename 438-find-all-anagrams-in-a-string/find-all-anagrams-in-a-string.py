class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        
        k = len(p)
        countp = Counter(p)
        check = Counter(s[:k])

        output = []
        if check == countp:
            output.append(0)

        for i in range(k , len(s)):
            check[s[i - k]] -= 1
            check[s[i]] += 1

            if check == countp:
                output.append(i - k + 1)

        return output

