# https://leetcode.com/problems/number-of-senior-citizens

from typing import List

class Solution:
    def countSeniors(self, details: List[str]) -> int:
        count_ages = 0
        for info in details:
            age = info[11:13]
            if int(age) > 60:
                count_ages += 1

        return count_ages