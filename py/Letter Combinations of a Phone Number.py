class Solution:
    def letterRecursive(self, digits: str, words: str, arr: List[str]):
        if len(digits) == 0:
            arr.append(words)
            return
        digit = int(digits[0])
        for x in self.dic[digit]:
            self.letterRecursive(digits[1:], words + x, arr)

    def letterCombinations(self, digits: str) -> List[str]:
        self.dic = {2:['a', 'b', 'c'],
        3:['d','e','f'],
        4:['g', 'h', 'i'],
        5:['j', 'k', 'l'],
        6:['m', 'n', 'o'],
        7:['p', 'q', 'r', 's'],
        8:['t','u', 'v'],
        9:['w', 'x', 'y', 'z'
        ]}
        arr = []
        if len(digits) > 0:
            self.letterRecursive(digits, "", arr)
        return arr
