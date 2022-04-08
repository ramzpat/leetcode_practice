# https://leetcode.com/problems/delete-and-earn/

class Solution(object):
    def deleteAndEarn(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        num_dict = {}
        distinc_nums = []
        for n in nums:
            if not( n in num_dict):
                num_dict[n] = n
                distinc_nums.append(n)
            else:
                num_dict[n] += n
                
        distinc_nums = sorted(distinc_nums)
        picked_sum = [0]*(len(distinc_nums)+1)
        picked_sum[1] = num_dict[distinc_nums[0]]

        for i in range(1, len(distinc_nums)):
            if(distinc_nums[i-1] == distinc_nums[i]-1):
                picked_sum[i+1] = max(num_dict[distinc_nums[i]] + picked_sum[i-1], picked_sum[i])
            else: 
                picked_sum[i+1] = num_dict[distinc_nums[i]] + picked_sum[i]
        return max(picked_sum[-1], picked_sum[-2])

s = Solution()

# print(s.deleteAndEarn([2,2,3,3,3,4]))
print(s.deleteAndEarn([1,1,1,2,4,5,5,5,6]))