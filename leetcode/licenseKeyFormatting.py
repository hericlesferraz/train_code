class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        s = s.replace("-", "").upper()
        
        first_group_length = len(s) % k or k        
        result = s[:first_group_length]
        
        for i in range(first_group_length, len(s), k):
            result += '-' + s[i:i + k]
        
        return result


Solution().licenseKeyFormatting(s='5F3Z-2e-9-w', k=4)
Solution().licenseKeyFormatting(s="2-5g-3-J", k=2)
