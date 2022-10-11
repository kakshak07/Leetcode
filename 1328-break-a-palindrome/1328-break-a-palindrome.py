class Solution:
    def breakPalindrome(self, palindrome: str) -> str:
#         n = len(palindrome)
#         for i in range(n//2):
#             if palindrome[i] != "a":
#                 return palindrome.replace(palindrome[i],"a",1)
#             return palindrome[:-1] + "b" if n>1 else ""
        
        
        l=len(palindrome)
        if l>1:
            for i in range(l//2):
                new=list(palindrome)
                if ord(new[i])>97:
                    new[i]='a'
                    return ''.join(new)
            new[l-1]='b'
            return ''.join(new)
        else:
            return ""