# https://leetcode.com/problems/count-vowel-strings-in-ranges/

from typing import List

class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        vowels = {"a", "e", "i", "o", "u"}
        prefix_sum = [0]
        for word in words:
            is_valid = word[0] in vowels and word[-1] in vowels
            prefix_sum.append(prefix_sum[-1] + (1 if is_valid else 0))
        
        answers = []
        for li, ri in queries:
            answers.append(prefix_sum[ri + 1] - prefix_sum[li])
        
        return answers

Solution().vowelStrings(words = ["aba","bcb","ece","aa","e"], queries = [[0,2],[1,4],[1,1]])
Solution().vowelStrings(words = ["a","e","i"], queries = [[0,2],[0,1],[2,2]])    