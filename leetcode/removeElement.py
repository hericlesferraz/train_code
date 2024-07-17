from typing import List

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        for number in sorted(nums):
            if number == val:
                nums.remove(val)
        print(nums)
        return len(nums)
    
Solution().removeElement(nums=[0,1,2,2,3,0,4,2], val=2)