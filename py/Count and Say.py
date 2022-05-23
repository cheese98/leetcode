class Solution:
    def countAndSay(self, n: int) -> str:
        if n == 1:
            return "1"
        prev = list(self.countAndSay(n-1))
        res = []
        i = 0
        while i < len(prev):
            count = 1
            val = prev[i]
            while i < len(prev) - 1 and prev[i] == prev[i+1]:
                count += 1
                i += 1
            res.append(str(count))
            res.append(val)
            i += 1
        return ''.join(res)
