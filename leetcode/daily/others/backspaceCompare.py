class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:        
        s = self.processString(s)
        t = self.processString(t)
        return s == t

    def processString(self, s: str) -> str:
        stack = []
        for char in s:
            if char == '#':
                if stack:
                    stack.pop()
            else:
                stack.append(char)
        return ''.join(stack)
    
Solution().backspaceCompare(s = "ab#c", t = "ad#c")
Solution().backspaceCompare(s = "ab##", t = "c#d#")
Solution().backspaceCompare(s = "a#c", t = "b")
Solution().backspaceCompare(s = "a##c", t = "#a#c")