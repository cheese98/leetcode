class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        N = (numRows - 1) * 2
        res = [""] * numRows
        for i in range(0, len(s)):
            pos = i % N if i % N < numRows else N - (i % N)
            res[pos] += s[i]
        return ''.join(res)
