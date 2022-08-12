# https://leetcode.com/problems/course-schedule/

from collections import defaultdict, deque
from typing import Dict, List
from urllib.robotparser import RequestRate
from xml.etree.ElementPath import prepare_self

class Gnode: 
  def __init__(self):
    self.in_degree = 0  
    self.out_edges = []


class Solution:
  def cycle_check_canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
    requireCourse:Dict[int, List[int]] = defaultdict(list)
    for a, b in prerequisites:
      requireCourse[a].append(b)

    check_courses = [False]*numCourses

    def noCycle(course, visited = {}):
      if check_courses[course]:
        return True
      if visited[course]:
        return False 
      visited[course] = True
      result = all([noCycle(rc, visited) for rc in requireCourse[course]]) 
      visited[course] = False
      check_courses[course] = True
      return result  
    
    for i in range(numCourses):
      if not check_courses[i]:
        visited = [False]*numCourses
        if not noCycle(i, visited):
          return False
    return True 

  # Topology sort
  def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

    # Key: course_id, Valie: Gnode
    graphNode:Dict[int, Gnode] = defaultdict(Gnode)
    # For checking the number of edges/dependencies 
    totalDependency = 0
    for [course, required_course] in prerequisites:
      graphNode[course].out_edges.append(required_course)
      graphNode[required_course].in_degree += 1
      totalDependency += 1 

    # Collected non-prerequisited courses 
    no_prereq_course = [course for course in range(numCourses) if graphNode[course].in_degree == 0]

    removedDependencies = 0
    while len(no_prereq_course) > 0:
      course = no_prereq_course.pop()

      for prereq_course in graphNode[course].out_edges:
        # Remove the dependency 
        graphNode[prereq_course].in_degree -= 1
        removedDependencies += 1

        # Consider the next course if there is no longer a prequisit course
        if graphNode[prereq_course].in_degree == 0:
          no_prereq_course.append(prereq_course)
    
    if removedDependencies != totalDependency:
      # There are edges left, we cannot finish the course 
      return False 
    return True 


