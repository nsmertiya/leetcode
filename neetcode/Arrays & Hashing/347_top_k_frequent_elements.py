class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        d = {}
        # dictionary for storing element and their count
        for num in nums:
            if num in d:
                d[num]+=1
            else:
                d[num]=1
        
        # sort the dictionary based value and keep only k elementss from the end
        sorted_d = sorted(d.items(), key=lambda x: x[1])[-k:]
        # convert to list as it has value along as well
        
        sorted_d = [val[0] for val in sorted_d]
        return sorted_d[:k]
        
        
solution = Solution()
print(solution.topKFrequent("a", "ab"))