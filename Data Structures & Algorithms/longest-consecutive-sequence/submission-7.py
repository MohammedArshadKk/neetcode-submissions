class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        longest=1;
        numsSet= set(nums)
        
        for num in nums:
           if num-1 not in numsSet:
            current= 1
            while(num+current in numsSet):
                current += 1
            longest = max(longest, current)                
        return longest