#
# @lc app=leetcode id=20 lang=python3
#
# [20] Valid Parentheses
#

# @lc code=start

# stack [1/5]
# iterate char in string:
#   if char is left sign, push to stack
#   if char is right sign, check if top of stack is corresponding left sign, if so pop, if not return false
# key: return true is stack is empty (all left signs have corresponding right sign)

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        lefts = ['(', '[', '{']

        for char in s:
            if char in lefts:
                stack.append(char)
            else:
                if stack == []:
                    return False

                top = stack.pop()
                if (char == ')' and top == '(') or (char == ']' and top == '[') or (char == '}' and top == '{'):
                    continue
                else:
                    return False

        return True if stack == [] else False

# @lc code=end
