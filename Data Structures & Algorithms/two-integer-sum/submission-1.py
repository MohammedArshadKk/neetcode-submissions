class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map={}
        for i in range(len(nums)):
            tar = target - nums[i];
            if tar in map:
                return [map[tar], i]
            else:
                map[nums[i]]=i 
      
              
        