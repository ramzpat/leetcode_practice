# https://leetcode.com/problems/average-salary-excluding-the-minimum-and-maximum-salary/

class Solution(object):
    def average(self, salary):
        """
        :type salary: List[int]
        :rtype: float
        """
        min_salary = salary[0]
        max_salary = salary[0]
        sum = salary[0]
        for i in range(1, len(salary)):
            max_salary = max(max_salary, salary[i])
            min_salary = min(min_salary, salary[i])
            sum += salary[i]
        return float(sum - max_salary - min_salary) / float(len(salary)-2)
            
s = Solution()
print(s.average(
[48000,59000,99000,13000,78000,45000,31000,17000,39000,37000,93000,77000,33000,28000,4000,54000,67000,6000,1000,11000]))