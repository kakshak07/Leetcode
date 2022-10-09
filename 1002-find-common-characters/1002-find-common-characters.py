class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        
        t = words[0]
        list_arr = []
        for i in t:
            xy = 0
            for k in range(1, len(words)):
                if i in words[k]:
                    words[k] = words[k].replace(i, "", 1)
                else:
                    break
                if k==len(words)-1:
                    xy = 1
            if xy == 1:
                list_arr.append(i)
        return(list_arr)
                
            
                