class Solution:
    def subarrayBitwiseORs(self, arr: list[int]) -> int:
        ans = set()
        endwithThis = set()
        for n in arr:
            endwithThis = {n | x for x in endwithThis}
            endwithThis.add(n)
            ans |= endwithThis
        return len(ans)