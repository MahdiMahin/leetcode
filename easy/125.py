class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        newstr=""
        s=s.lower()
        for char in s:
            if char.isalnum():
                newstr+=char
        return newstr==newstr[::-1]
    