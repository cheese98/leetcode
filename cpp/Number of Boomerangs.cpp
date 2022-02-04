class Solution {
public:
    int dist(vector<int> a, vector<int> b) {
		return (a[0] - b[0]) * (a[0] - b[0]) + (a[1] - b[1]) * (a[1] - b[1]);
	}
    
	int numberOfBoomerangs(vector<vector<int>>& points) {
		int n = points.size();
		if (n < 3) return 0;
		int count = 0;
        map<int, int> mapp;
		for (int i = 0; i < n; i++) {
			for (int j = 0; j < n; j++) {
				if (i != j) {
					int dis = dist(points[i], points[j]);
					mapp[dis]++;
				}
			}
            for (pair<int, int> x : mapp) {
                count += x.second * (x.second - 1);
            }
            mapp.clear();
		}
		return count;
	}
};
