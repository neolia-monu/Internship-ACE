class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        """
        """
        if len(nums) == 0:
            return 0
            
        if len(nums) == 1:
            return nums[0]
        
        i = j = 0
        while i < len(nums):
            while j < len(nums) and nums[i] == nums[j]:
                j += 1
            if j >= len(nums):
                break
            nums[i + 1] = nums[j]
            i += 1
        
        nums[i] = nums[j - 1]
        return i+1

        """
         Optimized Code
        """

        if len(nums) == 0:
            return 0

        if len(nums) == 1:
            return nums[0]
        
        i = j = 0
        while j < len(nums) - 1: 
            if nums[j] != nums[j + 1]: 
                nums[i] = nums[j]
                i += 1
            j += 1
        
        nums[i] = nums[j]
        return i+1
