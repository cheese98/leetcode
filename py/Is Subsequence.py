class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if len(s) == 0:
            return True
        if len(s) > len(t):
            return False
        point = 0
        for i in range(len(t)):
            if s[point] == t[i]:
                point += 1
            if point == len(s):
                return True
        return False
