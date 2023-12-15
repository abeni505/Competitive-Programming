class AuthenticationManager:

    def __init__(self, timeToLive: int):
        self.age = {}
        self.tTL = timeToLive
        

    def generate(self, tokenId: str, currentTime: int) -> None:
        self.age[tokenId] = currentTime + self.tTL
        

    def renew(self, tokenId: str, currentTime: int) -> None:
        if currentTime < self.age.get(tokenId,0):
            self.age[tokenId] = currentTime + self.tTL

    def countUnexpiredTokens(self, currentTime: int) -> int:
        count = 0
        for id, val in self.age.items():
            if val > currentTime:
                count += 1

        return count
        


# Your AuthenticationManager object will be instantiated and called as such:
# obj = AuthenticationManager(timeToLive)
# obj.generate(tokenId,currentTime)
# obj.renew(tokenId,currentTime)
# param_3 = obj.countUnexpiredTokens(currentTime)