class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        for i in range(len(digits)):
            digits[i]=str(digits[i])
        t="".join(digits)
        # t=string(digits)
        # print(t)
        o=int(t)+1
        w=str(o)
        return(list(w))
        # print(o)