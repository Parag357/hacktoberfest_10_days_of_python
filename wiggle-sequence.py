# A wiggle sequence is a sequence where the differences between successive numbers strictly alternate between positive and negative. 
# The first difference (if one exists) may be either positive or negative. A sequence with one element and a sequence with two non-equal elements are trivially wiggle sequences.

class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        n=len(nums)
        @lru_cache()
        def f(prev,curr,t):
            nonlocal nums,n
            if curr >= n: return 0
            p=nums[curr]-nums[prev]
            s=0
            if (p > 0 and not t) or (p < 0 and t):
                s=1+f(curr,curr+1,(not t))
            return max(f(prev,curr+1,t),s)
        return 1 + max(f(0,1,False),f(0,1,True))
