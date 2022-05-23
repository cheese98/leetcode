class BrowserHistory:

    def __init__(self, homepage: str):
        self.stack = [homepage]
        self.idx = 0

    def visit(self, url: str) -> None:
        self.idx += 1
        self.stack = self.stack[:self.idx] + [url]
        # print(self.stack)

    def back(self, steps: int) -> str:
        self.idx = max(self.idx - steps, 0)
        # print(self.stack)
        return self.stack[self.idx]

    def forward(self, steps: int) -> str:
        self.idx = min(self.idx + steps, len(self.stack) - 1)
        # print(self.stack)
        return self.stack[self.idx]


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)
