class Solution(object):
    def countKeyChanges(self, s):
        count=0
        for i in range (len(s)-1):
            if s[i].upper()!=s[i+1].upper():
                count+=1
        return count
solution=Solution()
