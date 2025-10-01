class Solution(object):
    def threeSum(self, nums):
        result=list(list())
        
        if(len(nums)<3):
            return result
        
        nums=sorted(nums)
        #print(nums)
        for i in range(len(nums)-2):
            if(i>0 and nums[i]==nums[i-1]):
                continue
            if(nums[i]>0):
                break
            low=i+1
            high=len(nums)-1
            while(low<high):
                res=nums[i]+nums[low]+nums[high]
                if(res==0):
                    triplet=[nums[i],nums[low],nums[high]]
                    # triplet=sorted(triplet)
                    if(triplet not in result):
                        result.append(triplet)
                    low=low+1
                    high=high-1
                    
                    while(low<high and nums[low]==nums[low-1]):
                        low=low+1
                    while(low<high and nums[high]==nums[high+1]):
                        high=high-1
                elif(res>0):
                    high=high-1
                else:
                    low=low+1
        return result
