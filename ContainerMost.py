class Solution(object):
    def maxArea(self, height):
        low=0
        high=len(height)-1
        maxi=0
        while(low<high):
            area=min(height[low],height[high])*(high-low)
            maxi=max(maxi, area)
            if(height[low]<=height[high]):
                low=low+1
            else:
                high=high-1
        return maxi
