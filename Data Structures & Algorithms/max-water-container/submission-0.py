from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:
        beg = 0
        end = len(height) - 1
        max_area = 0

        while beg < end:
            # Calculate current area
            area = min(height[beg], height[end]) * (end - beg)

            # Update maximum area
            max_area = max(max_area, area)

            # Move the pointer with the smaller height
            if height[beg] < height[end]:
                beg += 1
            else:
                end -= 1

        return max_area