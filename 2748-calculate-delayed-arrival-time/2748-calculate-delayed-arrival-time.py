class Solution:
    def findDelayedArrivalTime(self, arrivalTime: int, delayedTime: int) -> int:
        time=arrivalTime+delayedTime
        return time%24