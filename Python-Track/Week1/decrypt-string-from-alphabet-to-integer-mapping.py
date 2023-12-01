class Solution:
    def freqAlphabets(self, s: str) -> str:
        dict1 = {}
        new_str = ""
        char_int = ord('a')
        for i in range(1,27):
            dict1[i] =  chr(char_int)
            char_int += 1
        print(dict1)
        j = 0
        while j < len(s):
            if j+2 <len(s) and s[j+2] == "#":
                new_str += dict1[int(s[j:j+2])]
                j += 2

            else:

                new_str += dict1[int(s[j])]
            j+=1

        return new_str


            
