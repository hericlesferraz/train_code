from  typing import List
from collections import defaultdict

class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        
        fruit_count = defaultdict(int)
        left = 0
        max_fruits = 0
        
        for right in range(len(fruits)):
            fruit_count[fruits[right]] += 1
            
            while len(fruit_count) > 2:
                fruit_count[fruits[left]] -= 1
                if fruit_count[fruits[left]] == 0:
                    del fruit_count[fruits[left]]
                left += 1
            
            max_fruits = max(max_fruits, right - left + 1)
        
        return max_fruits


Solution().totalFruit(fruits=[1,2,1])
Solution().totalFruit(fruits=[0,1,2,2])
Solution().totalFruit(fruits=[1,2,3,2,2])