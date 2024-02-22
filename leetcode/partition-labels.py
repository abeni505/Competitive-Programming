class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        
        last_occur = defaultdict(int)
        for i in range(len(s)):
            last_occur[s[i]] = i

        i =0
        output = []
        while i < len(s):
            end = last_occur[s[i]]
            j = i + 1
            while j < end:
                if last_occur[s[j]] > end:
                    end = last_occur[s[j]]
                j += 1
            output.append( end - i +1)
            i = end + 1

        return output
            