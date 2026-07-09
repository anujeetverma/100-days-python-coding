class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        rot = k%n
        for _ in range (0,rot):
            e = nums.pop()
            nums.insert(0,e)