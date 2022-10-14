class Solution:
    def minSteps(self, s: str, t: str) -> int:
        couS = Counter(s)
        coun = 0
        for char in t:
            if char in couS and couS[char] > 0:
                couS[char] -= 1
            else:
                coun += 1


        couT = Counter(t)
        count = 0
        for char in s:
            if char in couT and couT[char] > 0:
                couT[char] -= 1
            else:
                count += 1

        return coun+count