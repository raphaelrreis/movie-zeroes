class Solution:
    def moveZeroes(self, nums):
        zero_pointer = 0
        for non_zero_pointer in range(len(nums)):
            if nums[non_zero_pointer] != 0:
                nums[zero_pointer], nums[non_zero_pointer] = nums[non_zero_pointer], nums[zero_pointer]
                zero_pointer += 1
