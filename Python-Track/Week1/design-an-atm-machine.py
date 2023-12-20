class ATM:

    def __init__(self):
        self.value = [20,50,100,200,500]
        self.hashmap = [0]*5

    def deposit(self, banknotesCount: List[int]) -> None:

        for i in range(len(banknotesCount)):
            if banknotesCount[i] > 0 :
                self.hashmap[i] += banknotesCount[i]
    

    def withdraw(self, amount: int) -> List[int]:
        
        withdrawal = [0, 0, 0, 0, 0]
        
        i = 4
        while i >= 0 and amount > 0:
            diff = amount // self.value[i]
            if self.hashmap[i] >= diff and amount >= self.value[i]:

                withdrawal[i] += diff
                amount -= (self.value[i] * diff)
            elif  0 <  self.hashmap[i] < diff and amount >= self.value[i] :
                withdrawal[i] += self.hashmap[i]
                amount -= (self.value[i] * self.hashmap[i])
            i -= 1

        

        if amount == 0:
            for i in range(5):
                self.hashmap[i] -= withdrawal[i]
            return withdrawal
        else:    
            return [-1]
            

# Your ATM object will be instantiated and called as such:
# obj = ATM()
# obj.deposit(banknotesCount)
# param_2 = obj.withdraw(amount)