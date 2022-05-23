class Solution {
public:
    int change(int amount, vector<int>& coins) {
        int dp[300][5001] = {0};
        for (int i = 0; i <= amount; i += coins[0]) {
            dp[0][i] = 1;
        }
        for (int i = 1; i < coins.size(); i++) {
            for (int j = 0; j <= amount; j++) {
                dp[i][j] += dp[i - 1][j];
                if (j - coins[i] >= 0)
                    dp[i][j] += dp[i][j - coins[i]];
            }
        }
        return dp[coins.size() - 1][amount];
    }
};
