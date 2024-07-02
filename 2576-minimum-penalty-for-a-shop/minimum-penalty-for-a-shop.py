class Solution:
    def bestClosingTime(self, customers: str) -> int:
        
        prefix_n = [0]
        postfix_y = [0]

        for i in customers:
            if i == "N":
                prefix_n.append(1)
            else:
                prefix_n.append(0)
                

        for j in range(len(customers) - 1,-1,-1):
            if customers[j] == "Y":
                postfix_y.append(1)
            else:
                postfix_y.append(0)

        prefix_n = list(accumulate(prefix_n))
        postfix_y = list(accumulate(postfix_y))
        postfix_y = postfix_y[::-1]
        
        total = [prefix_n[i] + postfix_y[i] for i in range(len(postfix_y))]

        # print(prefix_n)
        # print(postfix_y)
        # print(total)
        minn = min(total)
        
        return total.index(minn)