class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        
        counts = Counter(s)
        countt = Counter(t)

        if not s or not t:
            if not s:
                return t
            else:
                return s
                
        for key , val in countt.items():
            if key not in counts:
                return key
            
            if val != counts[key]:
                return key

        