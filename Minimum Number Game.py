class Solution(object):
    def numberGame(self, nums):
        arr = []
        while nums: 
            alice = min(nums)
            nums.remove(alice)  
            bob = min(nums)
            nums.remove(bob)
            arr.append(bob)
            arr.append(alice)
        return arr
solution = Solution()

