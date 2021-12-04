class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        N = (numRows - 1) * 2
        res = ["" for _ in range(0, numRows)]
        for i in range(0, len(s)):
            res[i % N if i % N < numRows else N - (i % N)] += s[i]
        return ''.join(res)
