class Solution:
    def findDelayedArrivalTime(self, arrivalTime: int, delayedTime: int) -> int:
        time=arrivalTime+delayedTime
        if time>=24:
            time=abs(24-time)
        
        return time