class Solution {
public:
    string longestPalindrome(string s) {
		string ans = "";
		for (int i = 0; i < s.size(); i++) {
			for (int j = 0; i - j >= 0 && i + j < s.size() ; j++) {
				if (s[i - j] != s[i + j]) break;
				if (ans.size() < 2 * j + 1) {
					ans = s.substr(i - j, 2 * j + 1);
				}
			}
			for (int j = 0; i - j >= 0 && i + j + 1 < s.size(); j++) {
				if (s[i - j] != s[i + j + 1]) break;
				if (ans.size() < 2 * j + 2) {
					ans = s.substr(i - j, 2 * j + 2);
				}
			}
		}
		return ans;
	}
};
