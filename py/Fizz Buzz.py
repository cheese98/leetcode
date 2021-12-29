class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        ans = []
        for i in range(1, n + 1):
            txt = ""
            if i % 3 == 0:
                txt += "Fizz"
            if i % 5 == 0:
                txt += "Buzz"
            if len(txt) == 0:
                txt = str(i)
            ans.append(txt)
        return ans
