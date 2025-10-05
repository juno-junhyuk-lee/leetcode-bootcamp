class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # Two Pointers
        left, right = 0, len(numbers)-1

        while left < right:
            # If the sum is target
            if numbers[left] + numbers[right] == target:
                return [left+1, right+1]
            
            # If the sum is greater than target
            if numbers[left] + numbers[right] > target:
                right -= 1
            
            # If the sum is less than target
            else:
                left += 1