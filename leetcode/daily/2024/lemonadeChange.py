# https://leetcode.com/problems/lemonade-change

from typing import List

class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        fives = 0
        tens = 0
        
        for bill in bills:
            if bill == 5:
                fives += 1
            elif bill == 10:
                if fives > 0:
                    fives -= 1
                    tens += 1
                else:
                    return False
            elif bill == 20:
                if tens > 0 and fives > 0:
                    tens -= 1
                    fives -= 1
                elif fives >= 3:
                    fives -= 3
                else:
                    return False
                
        return True

print(Solution().lemonadeChange(bills=[5,5,5,10,20]))
print(Solution().lemonadeChange(bills=[5,5,10,10,20]))
print(Solution().lemonadeChange(bills=[5,5,10,20,5,5,5,5,5,5,5,5,5,10,5,5,20,5,20,5]))
