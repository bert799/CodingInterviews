class Solution:
    def trap(self, height: list[int]) -> int:
        left_boundary, right_boundary = 0, 0 
        result = 0 

        l, r = 0, len(height)-1

        while l < r:
            left_boundary = max(left_boundary, height[l])
            right_boundary = max(right_boundary, height[r])

            if height[l] < height[r]:
                result += (left_boundary - height[l])
                l += 1
            else:
                result += (right_boundary - height[r])
                r -= 1
        
        return result 