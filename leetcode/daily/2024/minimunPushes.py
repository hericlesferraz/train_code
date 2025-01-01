#https://leetcode.com/problems/minimum-number-of-pushes-to-type-word-ii

class Solution:
    def minimumPushes(self, word: str) -> int:
        arr = [0] * 26
    
        for char in word:
            arr[ord(char) - ord('a')] += 1
        
        arr.sort(reverse=True)
        
        res = 0
        for i in range(len(arr)):
            res += arr[i] * ((i // 8) + 1)
        
        return res

print(Solution().minimumPushes(word="abcde"))
print(Solution().minimumPushes(word="xyzxyzxyzxyz"))