class Solution:
    def isSameAfterReversals(self, num: int) -> bool:
        if(num == 0):
            return(True)
        l = str(num)
        if(l[-1]=="0"):
            return(False)
        else:
            return(True)
        