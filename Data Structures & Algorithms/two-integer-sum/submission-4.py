class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}

        for i, value in enumerate(nums):
            diff = target - value
            if diff in seen: 
                return [seen[diff] , i]
            seen[value] = i
        