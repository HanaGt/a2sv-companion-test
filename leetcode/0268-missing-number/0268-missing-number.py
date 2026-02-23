class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        i = 0
        N = len(nums)

        while i < N:
            correct_idx = nums[i]

            if correct_idx < N and nums[correct_idx] != nums[i]:
                nums[correct_idx], nums[i] = nums[i], nums[correct_idx]
            else:
                i += 1

        for i in range(N):
            if nums[i] != i:
                return i 
        return N


