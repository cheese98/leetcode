class Solution {
public:
    map<int, int> visited;
	map<int, vector<int>> pre;
	vector<int> result;
	bool noCycle = true;

	void dfs(int cur) {
		visited[cur] = 1;
		for (int idx : pre[cur]) {
			if (visited[idx] == 0) {
				dfs(idx);
			}
			else if (visited[idx] == 1) {
				noCycle = false;
				return;
			}
		}
        result.push_back(cur);
		visited[cur] = 2;
	}

	vector<int> findOrder(int numCourses, vector<vector<int>>& prerequisites) {
		for (int i = 0; i < prerequisites.size(); i++) {
			pre[prerequisites[i][0]].push_back(prerequisites[i][1]);
		}
		for (int i = 0; i < numCourses && noCycle; i++) {
			if (visited[i] == 0) {
				dfs(i);
			}
		}
		if (!noCycle) result.clear();
		return result;
	}
};
