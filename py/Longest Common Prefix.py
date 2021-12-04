class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        word_len = len(strs[0])
        list_len = len(strs)
        for i in range(0, word_len):
            for j in range(0, list_len):
                if len(strs[j]) <= i or strs[j][i] != strs[0][i]:
                    return strs[0][:i]
        return strs[0]
