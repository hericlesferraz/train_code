# class Solution:
#     def countOfAtoms(self, formula: str) -> str:
#         dict_elements = {}
#         for index in range(0, len(formula)-2, 1):

#             current_element = formula[index]
#             next_element = formula[index+1]

#             if current_element.isupper() and next_element.isupper():
#                 dict_elements[str(current_element)] = 1

#             elif current_element.isupper() and next_element.islower():
#                 if formula[index+2].isupper():
#                     value = 1
#                 else:
#                     value = formula[index+2]
#                 dict_elements[f"{current_element}{next_element}"] = value
                
#             elif current_element.isupper() and next_element.isdigit():
#                 dict_elements[str(current_element)] = next_element
#                 print(current_element, next_element)

#         print(dict_elements)

# Solution().countOfAtoms(formula="H2MgO2")

class Solution:
    def countOfAtoms(self, formula: str) -> str:
        stack = [{}]
        i = 0
        n = len(formula)

        while i < n:
            if formula[i] == '(':
                stack.append({})
                i += 1
            elif formula[i] == ')':
                i += 1
                start = i
                while i < n and formula[i].isdigit():
                    i += 1
                multiplier = int(formula[start:i] or 1)
                top = stack.pop()
                for element, count in top.items():
                    if element in stack[-1]:
                        stack[-1][element] += count * multiplier
                    else:
                        stack[-1][element] = count * multiplier
            else:
                start = i
                i += 1
                while i < n and formula[i].islower():
                    i += 1
                element = formula[start:i]
                start = i
                while i < n and formula[i].isdigit():
                    i += 1
                count = int(formula[start:i] or 1)
                if element in stack[-1]:
                    stack[-1][element] += count
                else:
                    stack[-1][element] = count

        element_counts = stack.pop()
        result = []
        for element in sorted(element_counts.keys()):
            count = element_counts[element]
            result.append(f"{element}{count if count > 1 else ''}")
        return ''.join(result)

solution = Solution()
print(solution.countOfAtoms("H2O"))        # Output: "H2O"
print(solution.countOfAtoms("Mg(OH)2"))    # Output: "H2MgO2"
print(solution.countOfAtoms("K4(ON(SO3)2)2"))  # Output: "K4N2O14S4"
