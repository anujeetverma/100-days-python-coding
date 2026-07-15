class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        freq_map={}

        for i in range (0,n+1):
            freq_map[i] = 1
        
        for i  in nums:
            del freq_map[i]
        
        result = list(freq_map)
        return result[0]