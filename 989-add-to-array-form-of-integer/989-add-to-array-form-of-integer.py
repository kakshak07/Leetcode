class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        for i in range(len(num)):
            num[i]=str(num[i])
        e="".join(num)
        e=int(e)
        e=e+k
        qw=str(e)
        return(list(qw))
        