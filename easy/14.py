class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        minLength = min(strs,key=len)
        prefix = ""
        for i in range(len(minLength)):
            for word in strs:
                if word[i]!=strs[0][i]:
                    return prefix
            prefix += strs[0][i]
        return prefix

 

        


