class Solution:
    def removeComments(self, source: List[str]) -> List[str]:
        
      
        new_s = []
        for i in source:
            new_s += i
            new_s += "'"
            
        for i in range(len(new_s)):
            j = i + 2
            while j < len(new_s):

                if new_s[i] == "/" and new_s[i+1] == "*" and new_s[j] =="*" and new_s[j+1]=="/":
                    new_s = new_s[:i] + new_s[j+2:]
                    j = i + 2
                    

                elif new_s[i] == "/" and new_s[i+1] == "/" and new_s[j] == "'":
                    new_s = new_s[:i] + new_s[j:]
                    j = i + 2
                else:
                    j += 1
                    
        
        new_s = "".join(new_s)
        new_s  = new_s.split("'")
        while new_s.count(""):
            new_s.remove("")
        
        return new_s
