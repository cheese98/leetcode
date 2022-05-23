class Solution:
    def treeDP(self, k):
        if self.DP[k] != 0:
            return self.DP[k]
        res = 0
        for i in range(k):
            res += self.treeDP(i) * self.treeDP(k - i - 1)
        self.DP[k] = res
        return res

    def numTrees(self, n: int) -> int:
        self.DP = [0] * 20
        self.DP[0] = 1
        self.DP[1] = 1
        self.DP[2] = 2
        self.treeDP(n)
        return self.DP[n]
