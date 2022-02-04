class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
		if (strs.size() == 0) return vector<vector<string>>();
		map<vector<int>, vector<string>> mapp;
		for (string s : strs) {
			vector<int> parsed(26);
			for (char a : s) parsed[a - 'a']++;
			mapp[parsed].push_back(s);
		}
		vector<vector<string>> ans;
		for (auto x : mapp) {
			ans.push_back(x.second);
		}
		return ans;
	}
};
