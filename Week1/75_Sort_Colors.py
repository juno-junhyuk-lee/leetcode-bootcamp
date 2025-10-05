from collections import defaultdict

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        counter = defaultdict(int)

        for n in nums:
            counter[n] += 1
        
        i = 0
        for color in range(3):
            for _ in range(counter[color]):
                nums[i] = color
                i += 1

        