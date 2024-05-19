class Solution:
    def isValid(self, s: str) -> bool:
        dic = {'(' : ')', '[' : ']', '{' : '}'}
        lst = []

        for char in s:
            if char in dic:
                lst.append(dic[char])
            elif len(lst) > 0 and char == lst[-1]:
                lst.pop()
            else:
                return False
        return len(lst) == 0