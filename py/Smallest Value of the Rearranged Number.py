class Solution:
    def smallestNumber(self, num: int) -> int:
        if num == 0:
            return 0
        is_positive = num > 0
        num = abs(num)
        lyst = [0] * 10
        while num > 0:
            lyst[num % 10] += 1
            num //= 10
        ans = 0
        if is_positive:
            i = 1
            while lyst[i] == 0 and i < 10:
                i += 1
            ans = i
            lyst[i] -= 1
            for j in range(lyst[0]):
                ans *= 10
            for j in range(i, 10):
                for k in range(lyst[j]):
                    ans = ans * 10 + j
        else:
            for i in range(9, -1, -1):
                for j in range(lyst[i]):
                    ans = ans * 10 + i
            ans *= -1
        return ans
