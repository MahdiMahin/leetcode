class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        #find needle in haystack
        #sad in sadbutsad  
        for i in range(len(haystack)- len(needle)+1):
            if haystack[i:i+len(needle)]==needle:
                return i
        return -1
