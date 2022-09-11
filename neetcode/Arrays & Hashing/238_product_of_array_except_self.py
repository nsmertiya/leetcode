class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        """" create prefix variable for storing product of
             all numbers before the current number
             ex: [1,2,3,4]
             value of prefix for the value 4 in list will be 1*2*3 = 6
             
              create suffix variable for storing product of
             all numbers after the current number
             ex: [1,2,3,4]
             value of suffix for the value 1 in list will be 2*3*4 = 24
             
             result array for storing the final results, so for the number
             in the array, the product of all other numbers would be suffix * prefix
             ex: [1,2,3,4]
             
             prefix_array = [1,1,2,6]
             suffix_array = [24,12,4,1]
             result = [1*24,1*12,2*4,6*1]
             
        """
        
        prefix,suffix = 1,1
        result = len(nums)*[1]
        
        for i in range(len(nums)):
            result[i] = prefix
            prefix*=nums[i]
        
        
        for i in range(len(nums)-1,-1,-1):
            result[i] = suffix * result[i]
            suffix*=nums[i]
            
        return result
            
solution = Solution()
solution.productExceptSelf([1,2,3,4])        
        
        
        