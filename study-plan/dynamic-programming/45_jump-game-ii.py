# https://leetcode.com/problems/jump-game-ii/

class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        max_index = 0
        min_jump = {}
        min_jump[max_index] = 0
        max_jump_indexes = [0]
        i = 0

        def search_index(arr, target):
            left, right = 0, len(arr)-1
            ret = -1
            while(left <= right):
                mid = (left+right) // 2
                if (arr[mid] == target):
                    return mid
                elif (arr[mid] > target):
                    ret = mid
                    right = mid - 1
                else:
                    left = mid + 1
            return ret 

        while (max_index < n-1) and (i < n-1):
            next_max_index = nums[i] + i
            if (next_max_index > max_index):
                max_index = next_max_index
                max_jump_indexes.append(next_max_index)

                current_min_jump_index = search_index(max_jump_indexes, i)
                # print(max_jump_indexes)
                # print(min_jump)
                # print(max_jump_indexes[current_min_jump_index])
                min_jump[max_jump_indexes[-1]] = min(min_jump[max_jump_indexes[current_min_jump_index]] + 1, min_jump[max_jump_indexes[-2]] + 1)
            i += 1
        current_min_jump_index = search_index(max_jump_indexes, n-1)
        return min_jump[max_jump_indexes[current_min_jump_index]]

s = Solution()
print(s.jump([2,3,1,1,4]))
print(s.jump([2,3,0,1,4]))
print(s.jump([2]))
print(s.jump([7,0,9,6,9,6,1,7,9,0,1,2,9,0,3]))
