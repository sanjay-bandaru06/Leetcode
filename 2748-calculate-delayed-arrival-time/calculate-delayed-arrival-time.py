class Solution:
    def findDelayedArrivalTime(self, arrivalTime: int, delayedTime: int) -> int:
        Totaltime =( arrivalTime+delayedTime)%24
        # Totaltime2 = ( arrivalTime-delayedTime)
        # if Totaltime == 24:
        #     return 0
        # if Totaltime >24:
        #     return Totaltime2
        return Totaltime