class Solution:
    def smallestNumber(self, num: int) -> int:
        str_num = str(num)
        s = []
        for i in str_num:
            s.append(i)
        
        def positive (s):
            for i in range(len(s)):
                for j in range(len(s) - 1 - i):
                    if s[j + 1] < s[j]:
                        s[j] , s[j + 1] = s[j + 1] , s[j]
            if s[0] == '0':

                x = str(int("".join(s)))[0]
                # print(s)
                # print(x)
                y = s.index(x)
                s[0] , s[y] = s[y] , s[0]
                # print(s)

            ans = "".join(s)
            ans = int(ans)
            # print(ans)
            return ans
        def negative(s):
            for i in range(len(s)):
                for j in range(len(s) - 1 - i):
                    if s[j + 1] > s[j]:
                        s[j] , s[j + 1] = s[j + 1] , s[j]
            s.pop()
            
            ans = "".join(s)
            ans = int(ans) * -1
            # print(ans)
            return ans

        if num >= 0:
            return positive(s)
        else:
            return negative(s)
        
      
        