class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:

        prefix = {0:1}

        prefix_sum = 0
        count = 0

        for num in nums:
            prefix_sum += num

            if  (prefix_sum - k) in prefix:
                count += prefix[prefix_sum - k] 
                
            if prefix_sum in prefix:
                prefix[prefix_sum] += 1
            else:
                prefix[prefix_sum] = 1
        return count




        