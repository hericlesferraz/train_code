# https://leetcode.com/problems/make-two-arrays-equal-by-reversing-subarrays

from collections import Counter
from typing import List

class Solution:
    def canBeEqual(self, target: List[int], arr: List[int]) -> bool:
        return Counter(target) == Counter(arr)
    

Solution().canBeEqual(target = [1,2,3,4], arr = [2,4,1,3])
Solution().canBeEqual(target = [3,7,9], arr = [3,7,11])