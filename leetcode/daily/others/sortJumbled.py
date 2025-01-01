from typing import List
from collections import Counter


class Solution:
    def sortJumbled(self, mapping: List[int], nums: List[int]) -> List[int]:

        mapped_list = []
        for i, num in enumerate(nums):
            s = str(num)
            n = ''.join(str(mapping[int(ch)]) for ch in s)
            mapped_list.append((num, int(n), i))

        mapped_list.sort(key=lambda x: (x[1], x[2]))

        sorted_nums = [t[0] for t in mapped_list]

        return sorted_nums
    
Solution().sortJumbled(mapping = [8,9,4,0,2,1,3,5,7,6], nums = [991,338,38])