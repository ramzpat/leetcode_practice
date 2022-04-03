# https://leetcode.com/contest/weekly-contest-287/problems/maximum-candies-allocated-to-k-children/

class Solution(object):
    # binary search
    def maximumCandies(self, candies, k):
        """
        :type candies: List[int]
        :type k: int
        :rtype: int
        """
        max = candies[0]
        for i in range(1, len(candies)):
            if (max < candies[i]):
                max = candies[i]

        (left, right) = (1, max+1)
        max_candies = 0
        while(left <= right):
            mid = (left+right)/2
            sum = 0
            for candy in candies:
                sum += (candy/mid)
            if (sum >= k):
                max_candies = mid
                left = mid+1
            else:
                right = mid-1
        return max_candies

s = Solution()
ret = s.maximumCandies([2,5], 11)
print(ret)
# ret = s.maximumCandies([5,8,6], 3)
# print(ret)
# ret = s.maximumCandies([1,2,3,4,10], 5)
# print(ret) # 3 


# ret = s.maximumCandies([4,7,5], 4)
# print(ret) # 2