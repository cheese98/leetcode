class Solution {
    // need to optimize
public:
    int cutString(string x) {
		int a[26] = { 0 }, b[26] = { 0 };
		if (x.size() == 0 || x.at(0) == ' ') return -1;
		for (int i = 0; i < x.size(); i++) {
			b[x.at(i) - 'a']++;
		}
		for (int i = 0; i < x.size() - 1; i++) {
			b[x.at(i) - 'a']--;
			a[x.at(i) - 'a']++;
			int j;
			for (j = 0; j < 26; j++) {
				if (a[j] * b[j] != 0) break;
			}
			if (j == 26) {
				return i;
			}
		}
		return -1;
	}

	vector<int> partitionLabels(string s) {
		vector<string> parts;
		parts.push_back(s);
		bool flag = true;
		while (flag) {
			vector<string> new_parts;
			flag = false;
			for (string ss : parts) {
				int idx = cutString(ss);
				if (idx > -1) {
					new_parts.push_back(ss.substr(0, idx + 1));
					new_parts.push_back(ss.substr(idx + 1, ss.size() - 1));
					flag = true;
				}
				else {
					new_parts.push_back(string(ss.size(), ' '));
				}
			}
			parts = new_parts;
		}
		vector<int> ans;
		for (string ss : parts) {
			ans.push_back(ss.size());
		}
		return ans;
	}
};
