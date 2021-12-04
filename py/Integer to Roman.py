class Solution:
    def intToRoman(self, num: int) -> str:
        map = [["", "M", "MM", "MMM"],
               ["", "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM"],
               ["", "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"],
               ["", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"]]
        each = [num // 1000, (num // 100) % 10, (num // 10) % 10, num % 10]
        return map[0][each[0]] + map[1][each[1]] + map[2][each[2]] + map[3][each[3]]
