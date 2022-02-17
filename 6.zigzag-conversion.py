#
# @lc app=leetcode id=6 lang=python3
#
# [6] Zigzag Conversion
#

# @lc code=start
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        # 2D array with numRows rows and len(s) / numRows + numRows - 2 cols
        # iterate, fill in char in cols and next zipped char based on count

        col = (len(s) // numRows - 1) * (numRows - 1) + 1
        print(col)
        matrix = [['' for _ in range(col)] for _ in range(numRows + 1)]

        zip_count = numRows - 1
        count = zip_count
        char_idx = 0

        for j in range(col):
            for i in range(numRows + 1):
                print(s[char_idx], i, j)
                if count == zip_count:
                    matrix[i][j] = s[char_idx]
                    char_idx += 1
                else:
                    matrix[count][j] = s[char_idx]
                    char_idx += 1
                    break

            count -= 1
            if count == 0:
                count = zip_count

        res = ''
        for i in range(numRows):
            for j in range(col):
                print(matrix[i][j])
                res += matrix[i][j]

        return res

# @lc code=end
