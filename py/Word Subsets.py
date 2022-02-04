class Solution:    
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        res = []
        kkey = [0] * 26
        for w2 in words2:
            freq = Counter(w2)
            for i in range(26):
                kkey[i] = max(kkey[i], freq[chr(97 + i)])
        for w1 in words1:
            freq = Counter(w1)
            flag = True
            for i in range(26):
                if freq[chr(97 + i)] < kkey[i]:
                    flag = False
                    break
            if flag:
                res.append(w1)
        return res
