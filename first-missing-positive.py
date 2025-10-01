# First missing positve

# Given an unsorted integer array nums. 
# Return the smallest positive integer that is not present in nums.

from typing import List


class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        i=0
        n=len(nums)
        while i < n:
            val=nums[i]
            if i+1 != val and nums[i] > 0 and val-1 < n and nums[i] != nums[val-1]:
                [nums[i], nums[val-1]]=[nums[val-1],nums[i]]
                
            else:
                i+=1
        i=0
        while i < n:
            if i+1 != nums[i]: return i+1
            i+=1
        return i+1
