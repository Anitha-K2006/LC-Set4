class Solution(object):
    def differenceOfSum(self, nums):
        sume=0
        for i in nums:
            sume=sume+i
        sumd=0
        for i in nums:
            if i>0 and i<=9:
               sumd=sumd+i
            else:
               while(i!=0):
                  rem=i%10
                  sumd=sumd+rem
                  i=i/10
        diff=sume-sumd
        return diff
solution=Solution()
