class Solution(object):
    def toLowerCase(self, s):
        lwr=""
        for i in s:
            if i>="A" and i<="Z":
                lwr=lwr+chr(ord(i)+32)
            else:
                lwr=lwr+i
        return lwr
solution=Solution()
