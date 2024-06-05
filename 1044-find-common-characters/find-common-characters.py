class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        
       
        output = []


        for i in set(words[0]):
            count = words[0].count(i)
            occur = 1


            for j in range(1,len(words)):
                if i in words[j]:
                    count = min(count,words[j].count(i))
                    occur += 1
                else:
                    break

            if occur == len(words):
                for x in range(count):
                    output.append(i)
        
        return output


        
