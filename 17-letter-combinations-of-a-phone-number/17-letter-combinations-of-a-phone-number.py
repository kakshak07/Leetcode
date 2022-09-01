class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        
        res = []
        d = {"2": 'abc',
             "3": 'def',
             "4": 'ghi',
             "5": 'jkl',
             "6": 'mno',
             "7": 'pqrs',
             "8": 'tuv',
             "9": 'wxyz'
            }
        
        def backtrack(currstring, i):
            if(len(currstring) == len(digits)):
                res.append(currstring)
                return
            for j in d[digits[i]]:
                backtrack(currstring+j, i+1)
        if(digits==""):
            return([])
        backtrack("",0)
        return(res)
        