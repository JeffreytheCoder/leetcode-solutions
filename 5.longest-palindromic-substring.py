#
# @lc app=leetcode id=5 lang=python3
#
# [5] Longest Palindromic Substring
#

# @lc code=start
class Solution:
    def longestPalindrome(self, s: str) -> str:
        # iterate char and search to left and right to get palindrome which center is the current char
        # also search for pair (current character with the right one)

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

    # O(n^2), space: O(1)


class Solution:
    def longestPalindrome(self, s: str) -> str:
        # dp[i][j] is whether s[i:j+1] is palindrome
        # if s[i] == s[j] and (j-i < 2 or dp[i + 1][j - 1]), dp[i][j]=true
        # iterate i reversely

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

    # O(n^2), space: O(n^2)

# @lc code=end
