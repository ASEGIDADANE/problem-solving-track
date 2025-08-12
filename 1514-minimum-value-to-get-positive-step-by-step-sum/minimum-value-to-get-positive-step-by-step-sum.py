class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        prefix_sum = [nums[0]]

        for i in range(1,len(nums)):
            prefix_sum.append((prefix_sum[i-1] + nums[i]))
        if min(prefix_sum) >= 0:
            return 1
        else:
           return 0 - min(prefix_sum) + 1
         
        
 
        