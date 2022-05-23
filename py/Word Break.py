class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [0] * len(s)
        i = 1000
        for word in wordDict:
            i = min(i, len(word))
            if word == s[:len(word)]:
                dp[len(word) - 1] = 1
        while i < len(s):
            if dp[i] == 0:
                for word in wordDict:
                    if i - len(word) + 1 >= 0:
                        comp = s[i - len(word) + 1:i+1]
                        if comp == word and dp[i - len(word)] == 1:
                            dp[i] = 1
                            break
            i += 1
        return dp[-1]
