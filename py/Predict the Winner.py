class Solution:
    def PredictTheWinner(self, nums: List[int]) -> bool:
        dp = [[0 for i in range(len(nums))] for j in range(len(nums))]
        # dp[i][j] = game of i ~ j
        total = sum(nums)
        for i in range(len(nums)):
            dp[i][i] = nums[i]
        for k in range(1, len(nums)):
            for i in range(0, len(nums) - k):
                # i ~ i + k
                if k % 2 == 0:
                    #P1
                    dp[i][i + k] = max(nums[i] + dp[i + 1][i + k], nums[i + k] + dp[i][i + k - 1])

                else:
                    #P2
                    dp[i][i + k] = min(dp[i][i + k - 1], dp[i + 1][i + k])
        
        if len(nums) % 2 == 1:
            P1 = dp[0][-1]
            P2 = total - dp[0][-1]
        else:
            P1 = total - dp[0][-1]
            P2 = dp[0][-1]
        return P1 >= P2
