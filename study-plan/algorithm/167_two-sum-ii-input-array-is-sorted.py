# https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/

class Solution(object):
    # O(N log N)
    def twoSumOrig(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        n = len(numbers)
        for i in range(0, n):
            left, right = i+1, n-1
            target_val = target - numbers[i]
            if (target_val >= numbers[i]):
                while (left <= right):
                    mid = (left + right)//2 
                    if (numbers[mid] == target_val):
                        return [i+1, mid+1]
                    elif (numbers[mid] > target_val):
                        right = mid - 1
                    else:
                        left = mid + 1
    
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        left, right = 0, len(numbers)-1
        while (numbers[left] + numbers[right] != target):
            if (numbers[left] + numbers[right] > target):
                right -= 1
            else:
                left += 1
        return [left+1, right+1]

