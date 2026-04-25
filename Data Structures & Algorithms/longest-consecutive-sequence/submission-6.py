class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        nums.sort()
        print(nums)
        prev= nums[0]
        res= 1
        longest=1
        for i in range(1,len(nums)):
            if  nums[i] == prev:
                continue
            if nums[i]-1==prev:  
                    res+=1
                    prev=nums[i]
            else :
                res=1 
            prev=nums[i]
            longest = max(longest,res)
            

        return longest  