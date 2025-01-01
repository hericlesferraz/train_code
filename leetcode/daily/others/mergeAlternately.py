class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        l_text = max(len(word1), len(word2))
        new_text = ''
        for i in range(l_text):
            if len(word1) <= i:
               new_text += word2[i]
               
            elif len(word2) <= i:
               new_text += word1[i]

            else:
                new_text += f"{word1[i]}{word2[i]}"

        return new_text

Solution().mergeAlternately(word1='abc', word2='ef')
Solution().mergeAlternately(word1 = "ab", word2 = "pqrs")