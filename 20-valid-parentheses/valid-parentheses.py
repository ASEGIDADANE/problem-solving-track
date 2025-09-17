class Solution:
    def isValid(self, s: str) -> bool:
        dict = {
            ')':'(',
            ']':'[',
            '}':'{'
        }

        stack = []

        for char in s:
            if not stack:
                stack.append(char)
            else:
                if char in dict and stack[-1] == dict[char]:
                    stack.pop()
                else:
                    stack.append(char)
        if not stack:
            return True
        else:
            return False



      



