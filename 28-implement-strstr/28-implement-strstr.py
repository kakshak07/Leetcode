class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        w=len(needle)
        
        for i in range(len(haystack)-w+1):
            if(haystack[i:i+w]==needle):
                return(i)
        if(len(haystack)==0 and len(needle)==0):
            return(0)
        return(-1)