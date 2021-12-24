class Solution {
public:
    bool isAnagram(string s, string t) {
		int mask_s[26] = { 0 };
		int mask_t[26] = { 0 };

		if (s.size() != t.size()) return false;
		for (int i = 0; i < s.size(); i++) {
			mask_s[s.at(i) - 'a']++;
			mask_t[t.at(i) - 'a']++;
		}
		for (int i = 0; i < 26; i++) {
			if (mask_s[i] != mask_t[i]) return false;
		}
		return true;
    }
};
