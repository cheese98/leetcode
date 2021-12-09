class Solution {
public:
    bool isPalindrome(string s) {
		string r = "";
		for (int i = 0; i < s.size(); i++) {
			if ((s[i] >= 'a' && s[i] <= 'z') || (s[i] >= '0' && s[i] <= '9')) {
				r.push_back(s[i]);
			}
			else if (s[i] >= 'A' && s[i] <= 'Z') {
				r.push_back((char)(s[i] - 'A' + 'a'));
			}
		}
		for (int i = (r.size() - 1) / 2; i >= 0; i--) {
			if (r[i] != r[r.size() - 1 - i]) return false;
		}
		return true;
	}
};
