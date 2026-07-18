class Solution:
    


    def findGCD(self, nums: List[int]) -> int:
        mini = 10001
        maxi = 0
        n = len(nums)
        for i in range(0,n):
            if nums[i] < mini:
                mini = nums[i]
            if nums[i] > maxi:
                maxi = nums[i]
        
        while mini != 0:
            rem = maxi%mini
            if rem == 0:
                return mini
            maxi = mini
            mini = rem


        
    



