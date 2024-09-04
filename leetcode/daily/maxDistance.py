from typing import List

class Solution:
    def maxDistance(self, arrays: List[List[int]]) -> int:
        min_val = arrays[0][0]
        max_val = arrays[0][-1]
        max_distance = 0
        
        for i in range(1, len(arrays)):
            current_array = arrays[i]
            
            distance1 = abs(current_array[-1] - min_val)
            distance2 = abs(max_val - current_array[0])
            
            max_distance = max(max_distance, distance1, distance2)
            
            min_val = min(min_val, current_array[0])
            max_val = max(max_val, current_array[-1])
        
        return max_distance
        
print(Solution().maxDistance(arrays=[[1,2,3],[4,5],[1,2,3]]))
print(Solution().maxDistance(arrays=[[1,4,5],[0,2]]))
print(Solution().maxDistance(arrays=[[1,4],[0,5]]))

