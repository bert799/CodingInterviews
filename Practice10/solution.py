class Solution:
    def jump(self, nums: list[int]) -> int:
        res, reach, end = 0, 0, 0
        n = len(nums)
        for i in range(n-1):
            reach = max(reach, i + nums[i])

            if end == i:
                end = reach
                res += 1

        return res