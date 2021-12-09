class Solution {
public:
    int singleNumber(vector<int>& nums) {
		unordered_set<int> s;
		for (int x : nums) {
			if (s.find(x) == s.end()) {
				s.insert(x);
			}
			else {
				s.erase(x);
			}
		}
		return *(s.begin());
	}
};
