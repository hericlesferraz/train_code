# https://leetcode.com/problems/integer-to-english-words

class Solution:
    base = {
        0: "Zero", 1: "One", 2: "Two", 3: "Three", 4: "Four", 5: "Five", 6: "Six", 7: "Seven",
        8: "Eight", 9: "Nine", 10: "Ten", 11: "Eleven", 12: "Twelve", 13: "Thirteen", 
        14: "Fourteen", 15: "Fifteen", 16: "Sixteen", 17: "Seventeen", 18: "Eighteen", 
        19: "Nineteen", 20: "Twenty", 30: "Thirty", 40: "Forty", 50: "Fifty", 
        60: "Sixty", 70: "Seventy", 80: "Eighty", 90: "Ninety", 
        100: "Hundred", 1000: "Thousand", 1000000: "Million", 1000000000: "Billion"
    }
    
    def numberToWords(self, num: int) -> str:
        if num == 0:
            return self.base[0]
        
        result = []
        for scale in (1000000000, 1000000, 1000, 1):
            if num >= scale:
                count, num = divmod(num, scale)
                if scale > 1:
                    result.append(self.convert_less_than_1000_in_words(count))
                    result.append(self.base[scale])
                else:
                    result.append(self.convert_less_than_1000_in_words(count))
        
        return ' '.join(result).strip()
    
    def convert_less_than_1000_in_words(self, num: int) -> str:
        if num == 0:
            return ""
        elif num < 20:
            return self.base[num]
        elif num < 100:
            tens, below_ten = divmod(num, 10)
            return self.base[tens * 10] + (' ' + self.base[below_ten] if below_ten else '')
        else:
            hundreds, below_hundred = divmod(num, 100)
            return self.base[hundreds] + ' ' + self.base[100] + (' ' + self.convert_less_than_1000_in_words(below_hundred) if below_hundred else '')


print(Solution().numberToWords(num=123))
print(Solution().numberToWords(num=12345))
print(Solution().numberToWords(num=1235467))