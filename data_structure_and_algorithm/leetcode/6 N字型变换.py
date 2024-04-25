class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows < 2:
            return s
        i, flag = 0, -1
        res = ['' for _ in range(numRows)]
        for c in s:
            res[i] += c
            if i == 0 or i == numRows - 1:
                flag = -flag
            i += flag
        return ''.join(res)

s = Solution()
print(s.convert("PAYPALISHIRING", 3))