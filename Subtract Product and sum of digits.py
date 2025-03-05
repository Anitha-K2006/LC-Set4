class Solution(object):
    def subtractProductAndSum(self, n):
        pro=1
        Sum=0
        while(n!=0):
             rem=n%10
             Sum=Sum+rem
             pro=pro*rem
             n=n//10
        res=pro-Sum
        return res
solution=Solution()
        
