class Solution {
public:
    bool containsDuplicate(vector<int>& nums) {
		set<int> s;
		for (int elem : nums) {
			if (s.find(elem) != s.end()) return true;
			s.insert(elem);
		}
		return false;
    }
};
