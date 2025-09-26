'''
Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.
'''

class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        # find the left max and right max for each index and subtract the height at that index with min  of left and right max
        # calculate left array
        left = [0 for i in range(n)]
        leftmax = height[0]
        for i in range(n):
            if height[i] > leftmax:
                leftmax = height[i]
            left[i] = leftmax 
        # calculate right array
        right = [0 for i in range(n)]
        rightmax = height[n-1]
        for i in range(n-1, -1, -1):
            if height[i] > rightmax:
                rightmax = height[i]
            right[i] = rightmax 
        # now calculate trapped water
        res = 0
        for i in range(n):
            mn = min(left[i], right[i])
            if height[i] < mn:
                res += mn-height[i]
        return res
