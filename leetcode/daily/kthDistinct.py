# https://leetcode.com/problems/kth-distinct-string-in-an-array

from typing import List
from collections import Counter

class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        hash_times = Counter(arr)
        distinct_strings = [string for string in arr if hash_times[string] == 1]

        if k <= len(distinct_strings):
            return distinct_strings[k-1]
        
        return ""
        
print(Solution().kthDistinct(arr=["d","b","c","b","c","a"], k=2))
print(Solution().kthDistinct(arr=["aaa","aa","a"], k=1))
print(Solution().kthDistinct(arr = ["a","b","a"], k = 3))
print(Solution().kthDistinct(arr = ["a","b","a","c"], k=2))
