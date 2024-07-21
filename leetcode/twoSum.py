from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            n = len(nums)-1
            while i < n:
                result = nums[i] + nums[n]
                if result == target:
                    return [i, n]
                n -= 1
            
#Solution().twoSum(nums=[2,7,11,15], target=9)

Solution().twoSum(nums=[3,2,4], target=6)
