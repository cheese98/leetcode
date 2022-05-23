class Solution {
public:
    string addSpaces(string s, vector<int>& spaces) {
		string r;
		int i, count = 0;
		for (i = 0; i < s.size(); i++) {
			if (count < spaces.size() && i == spaces[count]) {
				r.push_back(' ');
				count++;
			}
			r.push_back(s.at(i));
		}
		return r;
	}
};
