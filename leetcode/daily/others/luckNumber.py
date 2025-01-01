from typing import List

class Solution:
    def luckyNumbers (self, matrix: List[List[int]]) -> List[int]:
        
        rows = len(matrix)

        for i in range(rows):
            min_row = min(matrix[i])
            min_index = matrix[i].index(min_row)
            max_col = 0

            for j in range(rows):
                if matrix[j][min_index] >= max_col:
                    max_col = matrix[j][min_index]
            
            if min_row == max_col:
                return [max_col]
        
Solution().luckyNumbers(matrix=[[3,7,8],[9,11,13],[15,16,17]])
Solution().luckyNumbers(matrix=[[1,10,4,2],[9,3,8,7],[15,16,17,12]])
Solution().luckyNumbers(matrix=[[7,8],[1,2]])