class Solution(object):
    def sortedSquares(self, nums):
        res=[]
        for i in range(len(nums)):
            res[i]=nums[i] ** 2
        x=res.sort()
        return x
solution=Solution()     
