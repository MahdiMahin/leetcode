class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        #IV = 5-1
        #VI = 5+1
        romandic={
            "I":1,
            "V":5,
            "X":10,
            "L":50,
            "C":100,
            "D":500,
            "M":1000
         }
        integer = 0
        for i in range(len(s)-1):
            if romandic[s[i]]<romandic[s[i+1]]:
                integer-= romandic[s[i]]
            else:
                integer+= romandic[s[i]]
        integer+= romandic[s[-1]]
        return integer
