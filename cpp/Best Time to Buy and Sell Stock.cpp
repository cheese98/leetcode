class Solution {
public:
    int maxProfit(vector<int>& prices) {
		int p = 0, ans = 0;
		for (int i = 1; i < prices.size(); i++) {
			if (prices[p] > prices[i]) p = i;
			else ans = max(prices[i] - prices[p], ans);
		}
		return ans;
	}
};
