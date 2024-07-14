class Solution:
    def countOfAtoms(self, formula: str) -> str:
        d = defaultdict(int)
        current = ''
        stack = []
        n = len(formula)
        multi = divider = 1
        
        for i in range(n-1, -1, -1):
            if formula[i].isalpha():
                if ord(formula[i]) <= 90:
                    current = formula[i] + current 
                    d[current] += multi
                    multi //= divider
                    divider = 1
                    current = ''
                else:
                    current += formula[i]
            elif formula[i] == ')':
                if i+1<n and formula[i+1].isdigit():
                    total = formula[i+1]
                    j = i+2
                    while j < n and formula[j].isdigit():
                        total += formula[j]
                        j += 1
                    multi *= int(total)
                    stack.append(int(total))
                else:
                    stack.append(1)
            elif formula[i] == '(':
                multi //= stack.pop()
            elif formula[i-1].isalpha():
                total = formula[i]
                j = i+1
                while j < n and formula[j].isdigit():
                    total += formula[j]
                    j += 1
                divider = int(total)
                multi *= divider

        ans = ''
        for k, v in sorted(d.items(), key = lambda x: x[0]):
            if v > 1:
                ans += k+str(v)
            else:
                ans += k
        return ans
        