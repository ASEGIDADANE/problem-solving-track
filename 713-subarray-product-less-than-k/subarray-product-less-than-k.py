class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        count = 0
      
        products = 1
        left = 0


        for right in range(len(nums)):
            if  k <= 1:
                return 0 
            products *= nums[right]
            
            

            
            while products >= k:
                
                products //= nums[left]
                left += 1
          
            count += right - left + 1
        return count



        

        
        