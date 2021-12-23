class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        def division(x, y):
            q = 0
            for i in range(31, -1, -1):
                z = y << i
                if z <= x:
                    x -= z
                    q += 1 << i
            return q
        res = 0
        if dividend == 0:
            return 0
        if (dividend > 0) == (divisor > 0):
            res = division(abs(dividend), abs(divisor))
        else:
            res = -division(abs(dividend), abs(divisor))
        return min(max(-(2**31), res), 2**31 - 1)
