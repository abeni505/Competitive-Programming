class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        
        total =  numBottles + (numBottles - 1) // (numExchange - 1)
        return total