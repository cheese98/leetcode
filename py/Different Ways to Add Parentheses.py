class Solution:
    def evaluate(self, x, y, op):
        if op == '+': return x + y
        if op == '-': return x - y
        if op == '*': return x * y
    
    def calculate(self, curr):
        if curr.isdigit():
            return [int(curr)]
        if curr in self.memo:
            return self.memo[curr]
        res = []
        for i in range(len(curr)):
            if curr[i] in '+-*':
                left = self.calculate(curr[:i])
                right = self.calculate(curr[i+1:])
                for l in left:
                    for r in right:
                        res.append(self.evaluate(l, r, curr[i]))
        self.memo[curr] = res
        return res

    def diffWaysToCompute(self, expression: str) -> List[int]:
        self.memo = {}
        return self.calculate(expression)
