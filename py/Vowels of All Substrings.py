class Solution:
    def countVowels(self, word: str) -> int:
        num_vowel = 0
        is_vowel = [0 for i in range(len(word))]
        
        for i in range(len(word)):
            if word[i] in ['a', 'e', 'i', 'o', 'u']:
                is_vowel[i] = 1
                num_vowel += 1
        if num_vowel == 0:
            return 0
        mult = [0 for i in range(len(word))]
        mult[0] = len(word)
        idx = 0
        D = len(word)
        while idx < len(word) - 1:
            D -= 2
            idx += 1
            mult[idx] = mult[idx - 1] + D
        res = 0
        for i in range(len(word)):
            res += mult[i] * is_vowel[i]
        return res
