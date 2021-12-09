class Solution:
    def isHappy(self, n: int) -> bool:
        lis = []
        while True:
            if n in lis:
                return n == 1
            lis.append(n)
            sum = 0
            while n > 0:
                sum += (n % 10)**2
                n //= 10
            n = sum
