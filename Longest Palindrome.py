class Solution(object):
    def longestPalindrome(self, s):
        indexCount = len(s)
        beginningIndex = 0
        longestPalindrome = ''
        if len(s) == 1:
            longestPalindrome = s
        else:
            while beginningIndex < len(s):
                if s[beginningIndex:indexCount] == s[beginningIndex:indexCount][::-1]:
                    if len(s[beginningIndex:indexCount]) > len(longestPalindrome):
                        longestPalindrome = s[beginningIndex:indexCount]
                indexCount -= 1
                if indexCount == 0 :
                    indexCount = len(s)
                    beginningIndex += 1
        return longestPalindrome

        