class Solution(object):
    def titleToNumber(self, columnTitle):
        length=len(columnTitle)-1
        sum=0
        count=0
        for i in range(length,-1,-1):
            sum=sum+(ord(columnTitle[i])-64)*(26)**count
            count+=1
        return sum