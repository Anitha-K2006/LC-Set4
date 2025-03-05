class Solution(object):
    def maximumWealth(self, accounts):
        lst=[]
        for i in accounts:
            Sum=0
            for j in i:
                Sum=Sum+j
                lst.append(Sum)
        return max(lst)
solution=Solution()
        
