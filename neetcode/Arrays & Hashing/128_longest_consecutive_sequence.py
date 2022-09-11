class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        
        nums_set = set(nums)
        print(nums_set)
        
        result = 0
        temp = 0
        for num in nums:
            if num-1 not in nums_set:
                temp = 1
                while(num+temp) in nums_set:
                    temp+=1
            result = max(temp,result)

        return result
        
        

solution = Solution()
solution.longestConsecutive([0,-1])
        
        