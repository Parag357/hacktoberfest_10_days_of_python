'''
Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].
'''

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        helper = [1 for i in range(n)]
        pref = 1
        for i in range(1, n):
            pref = pref * nums[i-1]
            helper[i] = helper[i] * pref
        post = 1
        for i in range(n-2, -1, -1):
            post = post * nums[i+1]
            helper[i] = helper[i] * post
        return helper
