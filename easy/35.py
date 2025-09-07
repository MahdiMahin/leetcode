class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        curr_index=0
        for i in range(len(nums)):
            if target in nums: 
                return nums.index(target)
            elif nums[i]<target:
                curr_index=i+1
        return curr_index


        


        
#i=0 if 1<2,index = 1