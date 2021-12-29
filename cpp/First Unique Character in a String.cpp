class Solution {
public:
    int firstUniqChar(string s) {
		vector<int> map;
		for (int i = 0; i < 26; i++) map.push_back(100001);
		for (int i = 0; i < s.size(); i++) {
			if (map[s.at(i) - 'a'] == 100001) {
				map[s.at(i) - 'a'] = i;
			}
			else if (map[s.at(i) - 'a'] != -1) {
				map[s.at(i) - 'a'] = -1;
			}
		}
		int min = 100001;
		for (int x : map) {
			if (x != 100001 && x != -1) {
				min = min < x ? min : x;
			}
		}
		return min < 100001 ? min : -1;
    }
};
