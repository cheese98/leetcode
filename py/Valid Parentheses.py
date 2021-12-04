class Solution:
    def isValid(self, s: str) -> bool:
        par = []
        for i in s:
            if i == ')':
                if len(par) == 0 or par[-1] != '(':
                    return False
                par.pop()
            elif i == ']':
                if len(par) == 0 or par[-1] != '[':
                    return False
                par.pop()
            elif i == '}':
                if len(par) == 0 or par[-1] != '{':
                    return False
                par.pop()
            else:
                par.append(i)
        return len(par) == 0
