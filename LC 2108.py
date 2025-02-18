class Solution(object):
    def firstPalindrome(self, words):
        for i in words:
            t=i[ : :-1]
            if i==t:
               return i
        return ""
solution=Solution()
    
