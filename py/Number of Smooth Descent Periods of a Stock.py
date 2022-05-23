class Solution:
    def getDescentPeriods(self, prices: List[int]) -> int:
        #res = len(prices)
        res = 0
        counter = 1
        prices.append(-1)
        for i in range(1, len(prices)):
            if prices[i] == prices[i - 1] - 1:
                counter += 1
            else:
                print(i, int(counter * (counter + 1) / 2))
                res += int(counter * (counter + 1) / 2)
                counter = 1
        return res
