class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        if len(nums)<2 or len(nums)>1000 or target<-10000000 or target>10000000:
            return False 
        prev={}    
        for i in range(len(nums)):
            diff=target-nums[i]

            if diff in prev:
                return [prev[diff],i]

            prev[nums[i]]=i    