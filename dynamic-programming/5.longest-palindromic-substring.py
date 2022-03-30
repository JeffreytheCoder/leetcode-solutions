#
# @lc app=leetcode id=5 lang=python3
#
# [5] Longest Palindromic Substring
#

# @lc code=start

# iterative [2/5]
# iterate char:
#   inc left and dec right pointer to get largest palindrome which center is the current char
# also find largest palindrome which center is pair with same char (current character with the right one)
class Solution:
    def longestPalindrome(self, s: str) -> str:

        def getPalindrome(s: str, left: int, right: int, start: int, max_len: int):
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1

            new_len = right - left - 1
            if (max_len < new_len):
                start = left + 1
                max_len = new_len

            return start, max_len

        if len(s) < 2:
            return s

        start = max_len = 0

        for i in range(len(s) - 1):
            start, max_len = getPalindrome(s, i, i, start, max_len)
            start, max_len = getPalindrome(s, i, i + 1, start, max_len)

        return s[start: start + max_len]

# time: O(n^2)
# space: O(1)

# dp [4/5]
# dp[i][j] is whether s[i:j+1] is palindrome
# if s[i] == s[j] and (j-i < 2 (single or pair) or dp[i + 1][j - 1] (last character is palindrome)), dp[i][j]=true
# iterate i reversely
class Solution:
    def longestPalindrome(self, s: str) -> str:

        dp = [[False for _ in range(len(s))] for _ in range(len(s))]
        max_len = 0
        res = ''

        for i in range(len(s)):
            dp[i][i] = True
            res = s[i]

        for i in range(len(s) - 1, -1, -1):
            for j in range(i + 1, len(s)):
                if s[i] == s[j] and (j - i < 2 or dp[i + 1][j - 1]):
                    dp[i][j] = True

                    new_len = j - i + 1
                    if max_len < new_len:
                        max_len = new_len
                        res = s[i: j + 1]

        return res

# time: O(n^2)
# space: O(n^2)

# @lc code=end
