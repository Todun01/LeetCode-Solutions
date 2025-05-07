class Solution(object):
    def isPalindrome(self, x):
        isPalindrome = False
        num = str(x)[::-1]
        if num == str(x):
            isPalindrome = True
        return isPalindrome