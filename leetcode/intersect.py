# https://leetcode.com/problems/intersection-of-two-arrays-ii

from typing import List

class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:

        len_1 = len(nums1)
        len_2 = len(nums2)

        nums1 = sorted(nums1)
        nums2 = sorted(nums2)

        max_len = max(len_1, len_2)
        result = []

        for i in range(max_len):
            if len_1 >= len_2:

                if nums1[i] in nums2:
                    nums2.remove(nums1[i])
                    result.append(nums1[i])
                
            else:
                if nums2[i] in nums1:
                    nums1.remove(nums2[i])
                    result.append(nums2[i])
        return result
    
Solution().intersect(nums1=[1,2,2,1], nums2=[2,2])
Solution().intersect(nums1=[4,9,5], nums2=[9,4,9,8,4])
Solution().intersect(nums1=[3,1,2], nums2=[1,3])
