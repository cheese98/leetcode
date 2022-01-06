class Solution {
public:
    int height, width;

	int searchIsland(int p, int q, vector<vector<int>>& grid) {
		if (p < 0 || q < 0 || p >= height || q >= width || grid[p][q] == 0) {
			return 0;
		}
		grid[p][q] = 0;
		int ret = 1 + searchIsland(p - 1, q, grid) + searchIsland(p + 1, q, grid) + searchIsland(p, q - 1, grid) + searchIsland(p, q + 1, grid);
		return ret;
	}

	int maxAreaOfIsland(vector<vector<int>>& grid) {
		int max = 0;
		height = grid.size();
		width = grid[0].size();
		for (int i = 0; i < height; i++) {
			for (int j = 0; j < width; j++) {
				if (grid[i][j] == 1) {
					int size = searchIsland(i, j, grid);
					max = max < size ? size : max;
				}
			}
		}
		return max;
	}
};
