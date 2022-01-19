#
# @lc app=leetcode id=20 lang=python3
#
# [20] Valid Parentheses
#

# @lc code=start
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
