class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        i = 0

        while i < len(nums):

            if i > 0 and nums[i] == nums[i-1]:
                i += 1
                continue

            j, k = i+1, len(nums)-1

            while j<k:
                numsum = nums[i] + nums[j] + nums[k]

                if numsum == 0:
                    res.append([nums[i], nums[j], nums[k]])
                    j += 1

                    while j < k and nums[j] == nums[j-1]:
                        j+=1
                
                elif numsum < 0:
                    j += 1
                
                else:
                    k -=1
            i += 1

        return res