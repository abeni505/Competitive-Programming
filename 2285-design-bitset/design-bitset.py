class Bitset:

    def __init__(self, size: int):
        self.array = [0] * size
        self.fliped = [1] * size
        self.count_1 = 0
        

    def fix(self, idx: int) -> None:
        if self.array[idx] != 1:
            self.array[idx] = 1
            self.fliped[idx] = 0
        
            self.count_1 += 1
    
        

    def unfix(self, idx: int) -> None:
        if self.array[idx] != 0:
            self.array[idx] = 0
            self.fliped[idx] = 1

            self.count_1 -= 1
        

    def flip(self) -> None:
        self.array , self.fliped = self.fliped , self.array

        self.count_1 = len(self.array) - self.count_1

    def all(self) -> bool:
        return self.count_1 == len(self.array)
        

    def one(self) -> bool:
        return self.count_1 >= 1

    def count(self) -> int:
        return self.count_1
        

    def toString(self) -> str:
        out_put = ["1" if i else "0" for i in self.array]
        
        return "".join(out_put)
        


# Your Bitset object will be instantiated and called as such:
# obj = Bitset(size)
# obj.fix(idx)
# obj.unfix(idx)
# obj.flip()
# param_4 = obj.all()
# param_5 = obj.one()
# param_6 = obj.count()
# param_7 = obj.toString()