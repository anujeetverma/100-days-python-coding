class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        ans = []
        count = 0
        for i in range(0, n):
            if nums[i] != 0:
                ans.append(nums[i])
            if nums[i] == 0:
                count += 1
        for j in range(0, count):
            ans.append(0)
        nums[:] = ans
        
