from typing import List

class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        results = []
        
        def backtrack(start, current_combination, current_sum):
            if current_sum == target:
                results.append(list(current_combination))
                return
            if current_sum > target:
                return
            
            for i in range(start, len(candidates)):
                if i > start and candidates[i] == candidates[i - 1]:
                    continue
                
                current_combination.append(candidates[i])
                backtrack(i + 1, current_combination, current_sum + candidates[i])
                current_combination.pop() 
                
        backtrack(0, [], 0)

        return results

Solution().combinationSum2(candidates = [10,1,2,7,6,1,5], target = 8)