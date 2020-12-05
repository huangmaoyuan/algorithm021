class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        mapsum=dict()
        for i,x in enumerate(nums):
            if target-x in mapsum:
                return [mapsum[target-x],i]
            mapsum[x]=i
