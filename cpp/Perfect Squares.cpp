class Solution {
public:
    int numSquares(int n) {
		int i, j, r = 0;
		vector<int> sq = { 0 };
		for (i = 1; i <= n; i++) {
			sq.push_back(i);
		}
		for (r = 1; r * r <= n; r++) {
			sq[r * r] = 1;
		}
		for (i = 2; i <= r; i++) {
			int u = i * i;
			for (j = u + 1; j <= n; j++) {
				sq[j] = min(sq[j], sq[j - u] + 1);
			}
		}
		return sq[n];
	}
};
