class Solution:
    def romanToInt(self, s: str) -> int:
        hash_dict = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000,
        }

        result = 0
        rom_idx = 0

        while rom_idx < len(s)-1:
            if s[rom_idx] < s[rom_idx+1]:
                print('Menor', hash_dict[s[rom_idx+1]], hash_dict[s[rom_idx]])
                result += hash_dict[s[rom_idx+1]] - hash_dict[s[rom_idx]]
                rom_idx += 1
            else:
                result += hash_dict[s[rom_idx]]
                rom_idx += 1

        print(result)
        return result
    
Solution().romanToInt(s="III")
#Solution().romanToInt(s="LVIII")
#Solution().romanToInt(s="MCMXCIV")
