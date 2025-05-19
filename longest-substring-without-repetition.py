class Solution(object):
    def lengthOfLongestSubstring(self, s):
        longestSubString = ''
        charCount = 0
        subString = ''
        i = 0
        isDuplicate = False
        if len(s) == 1:
            return 1
        while i < len(s):
            if s[i] in subString:
                charCount += 1
                i = charCount
                isDuplicate = True
                if len(subString) > len(longestSubString):
                    longestSubString = subString
                subString = ''
            else:
                subString += s[i]
                isDuplicate = False
                i += 1
        if not isDuplicate and len(longestSubString) < len(subString):
            longestSubString = subString
        return len(longestSubString)


        