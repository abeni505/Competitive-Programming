class Solution:
    def minSteps(self, s: str, t: str) -> int:
     
        s = Counter(s)
        t = Counter(t)
        steps = 0
        for char, freq in s.items():
            
            if t[char] < freq:
                steps += freq - t[char]
                
        stepsback = 0
        for char, freq in t.items():
            
            if s[char] < freq:
                stepsback += freq - s[char]
         
        return min(steps, stepsback)