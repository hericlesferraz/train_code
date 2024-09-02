from typing import List

class Solution:
    def chalkReplacer(self, chalk: List[int], k: int) -> int:
        total_chalk = sum(chalk)
        k %= total_chalk 

        for i, amount in enumerate(chalk):
            if k < amount:
                return i
            k -= amount          

print(Solution().chalkReplacer(chalk=[5,1,5], k=22))
print(Solution().chalkReplacer(chalk=[3,4,1,2], k=25))