# https://leetcode.com/contest/weekly-contest-287/problems/find-players-with-zero-or-one-losses/

class Solution(object):
    def findWinners(self, matches):
        """
        :type matches: List[List[int]]
        :rtype: List[List[int]]
        """
        max_id = -1
        min_id = -1
        lost_cnt = {}
        for [winner, loser] in matches:
            if not (winner in lost_cnt):
                if (max_id < winner):
                    max_id = winner
                if (min_id > winner or min_id == -1):
                    min_id = winner
                lost_cnt[winner] = 0
            if not (loser in lost_cnt):
                if (max_id < loser):
                    max_id = loser
                if (min_id > loser or min_id == -1):
                    min_id = loser
                lost_cnt[loser] = 0
            if (lost_cnt[loser] < 2):
                lost_cnt[loser] = lost_cnt[loser] + 1
        
        no_lost = [x for x in range(min_id, max_id+1) if x in lost_cnt and lost_cnt[x] == 0]
        lost_one = [x for x in range(min_id, max_id+1) if x in lost_cnt and  lost_cnt[x] == 1]
        return [no_lost, lost_one]

s = Solution()
[a,b] = s.findWinners([[1,9],[1,14],[2,3],[2,7],[2,12],[2,15],[2,16],[2,17],[3,6],[3,7],[3,13],[3,15],[3,17],[3,18],[4,5],[4,8],[4,11],[4,19],[5,8],[5,9],[5,13],[5,17],[5,18],[6,10],[6,18],[7,11],[9,13],[10,11],[10,14],[10,17],[11,13],[11,16],[12,15],[12,17],[13,15],[14,18],[15,17],[15,19],[16,17],[16,19]])
print(a, b)
