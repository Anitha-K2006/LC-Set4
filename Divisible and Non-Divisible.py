class Solution(object):
    def differenceOfSums(self, n, m):
        num1=[]
        num2=[]
        for i in range(1,n+1):
            if i%m!=0:
               num1.append(i)
            else:
               num2.append(i)
        x=sum(num1)
        y=sum(num2)
        diff=x-y
        return diff
solution=Solution()
               
        
