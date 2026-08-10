class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_map = {}
        # nums_map = {-1: 0, 5: 1, -3: 2}
        for index in range(len(nums)):
            complement = target - nums[index]
            if complement in nums_map:
                print([nums_map[complement], index])
                return [nums_map[complement], index]
            nums_map[nums[index]] = index