class Solution:
    def containsDuplicate(self, nums) -> bool:

        # SOLUTION 1
        # create a list for storing any unique numer we identify
        unique_nums = set()

        for num in nums:
            # if num already present in set return True directly as a duplicate is found
            # else add it to unique_nums list
            if num in unique_nums:
                return True
            else:
                unique_nums.add(num)
        # return False if we are done iterating over all numbers, as no unique num is found
        return False


#         # SOLUTION 2
#         # create a set with the list and compare the len, if equal all are unique else false

#         unique_nums = set(nums)

#         if len(unique_nums)==len(nums):
#             return False
#         else:
#             return True
