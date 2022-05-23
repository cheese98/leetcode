class Solution {
public:
    vector<vector<int>> queensAttacktheKing(vector<vector<int>>& queens, vector<int>& king) {
		int board[8][8] = { 0 };
		vector<vector<int>> res;
		int dx[] = {0, -1, -1, -1, 0, 1, 1, 1};
		int dy[] = {1, 1, 0, -1, -1, -1, 0, 1};
		for (vector<int> queen : queens) {
			board[queen[0]][queen[1]] = 1;
		}
		for (int i = 0; i < 8; i++) {
			for (int x = king[0], y = king[1]; x >= 0 && x < 8 && y >= 0 && y < 8; x += dx[i], y += dy[i]) {
				if (board[x][y] == 1) {
					res.push_back({ x, y });
					break;
				}
			}
		}
		return res;
	}
};
