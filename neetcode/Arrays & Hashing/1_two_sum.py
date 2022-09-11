from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # SOLUTION 1, time complexity (O(N^2))
        # for i, numi in enumerate(nums):
        #     for j, numj in enumerate(nums):
        #         if numi + numj == target:
        #             if i == j:
        #                 continue
        #             else:
        #                 return list([i, j])

        # SOLUTION 2
        # store value with index in a dictionary
        all_nums = {}
        for i, num in enumerate(nums):
            # determine the second number
            second_number = target - num

            # if found return index, else add it to all_nums
            if second_number in all_nums:
                return [all_nums[second_number], i]

            all_nums[num] = i


solution = Solution()
print(solution.twoSum([2, 7, 11, 15], 9))
