class OrderedStream:

    def __init__(self, n: int):
        self.stream = [0] * n
        self.ptr = 0

    def insert(self, idKey: int, value: str) -> List[str]:
        id = idKey - 1
        self.stream[id] = value


        out_put = []
        if id == self.ptr:
            
            while self.ptr < len(self.stream):
                if self.stream[self.ptr] == 0:
                    break
                else:
                    out_put.append(self.stream[self.ptr])
                self.ptr += 1
        return out_put
        


# Your OrderedStream object will be instantiated and called as such:
# obj = OrderedStream(n)
# param_1 = obj.insert(idKey,value)