class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        """
            Brtue force approach
        """
        res = []
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    res.append(i)
                    res.append(j)

        return res

        """
            Second Method:
                Dictionary in python
        """
        res = []
        d = {}

        for i in range(len(nums)):
            if target - nums[i] in d:
                res.append(i)
                res.append(d[target - nums[i]])
                break
            d[nums[i]] = i
        return res