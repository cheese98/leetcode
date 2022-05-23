class Solution:
    def recursive(self, n, op, cl, par):
        if len(par) == n * 2:
            self.results.append(par)
        if op > cl:
            self.recursive(n, op, cl + 1, par + ')')
        if op < n:
            self.recursive(n, op + 1, cl, par + '(')
        
    def generateParenthesis(self, n: int) -> List[str]:
        self.results = []
        self.recursive(n, 0, 0, "")
        return self.results
