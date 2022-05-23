class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        sets = set()
        res = set()
        for i in range(len(s) - 9):
            seq = s[i:i+10]
            if seq in sets:
                res.add(seq)
            else:
                sets.add(seq)
        return list(res)
