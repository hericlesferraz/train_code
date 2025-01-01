from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        write_index = 1
        
        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1]:
                nums[write_index] = nums[i]
                write_index += 1

        return write_index
    
Solution().removeDuplicates(nums=[0,0,1,1,1,2,2,3,3,4])