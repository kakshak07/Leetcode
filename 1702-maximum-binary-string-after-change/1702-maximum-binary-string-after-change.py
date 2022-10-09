class Solution:
    def maximumBinaryString(self, binary: str) -> str:
        # binary = "1101110"
        t = binary.find("0")
        x = len(binary)
        a = binary.count("0")-1
        xy = t+a
        # print(xy)
        w = ""
        
        for i in range(len(binary)):
            if i ==xy:
                w=w+"0"
            else:
                w=w+"1"
        return(w)
        
        
        
        