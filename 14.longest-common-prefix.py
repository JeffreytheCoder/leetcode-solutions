#
# @lc app=leetcode id=14 lang=python3
#
# [14] Longest Common Prefix
#

# @lc code=start
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # key: longest possible prefix is the shortest string
        # solution: get the shortest string
        #   compare iterated substring of the shortest string to others, if not equal, return last equal substring

        prefix = min(strs, key=len)

        for i, char in enumerate(prefix):
            for str in strs:
                if str[i] != char:
                    return prefix[:i]

        return prefix

# @lc code=end
