# https://leetcode.com/contest/weekly-contest-287/problems/minimum-number-of-operations-to-convert-time/

class Solution(object):
    def convertTime(self, current, correct):
        """
        :type current: str
        :type correct: str
        :rtype: int
        """
        current_hr = int(current[0:2])
        current_min = int(current[3:5])

        correct_hr = int(correct[0:2])
        correct_min = int(correct[3:5])
        
        operation_cnt = 0
        # adjust minutes
        while (current_min != correct_min):
            if (current_min > correct_min):
                adjust_next_hr = 60
            else:
                adjust_next_hr = 0
            if (current_min + 15 <= correct_min + adjust_next_hr):
                operation_cnt = operation_cnt + 1
                current_min += 15
            elif (current_min + 5 <= correct_min + adjust_next_hr):
                operation_cnt = operation_cnt + 1
                current_min += 5
            elif (current_min + 1 <= correct_min + adjust_next_hr):
                operation_cnt = operation_cnt + 1
                current_min += 1
            if (current_min >= 60):
                current_min = current_min-60
                current_hr = current_hr + 1
            if (current_hr >= 24):
                current_hr = 0

        # adjust hour
        if (current_hr > correct_hr):
            operation_cnt = operation_cnt + (24-current_hr) + correct_hr
        elif (current_hr < correct_hr):
            operation_cnt = operation_cnt + (correct_hr-current_hr)

        return operation_cnt

s = Solution()
# ret = s.convertTime("11:00", "11:01")
ret = s.convertTime("02:12", "03:00")
print(ret)