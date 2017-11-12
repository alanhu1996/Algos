# There are a total of n courses you have to take, labeled from 0 to n - 1.

# Some courses may have prerequisites, for example to take course 0 you have to first take course 1, which is expressed as a pair: [0,1]

# Given the total number of courses and a list of prerequisite pairs, return the ordering of courses you should take to finish all courses.



import Queue
class Solution(object):
    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """
        
        inDegree = {}
        adjList = {}
        # Initialize in degree array for all the courses to be 0 at first.
        for i in range(numCourses):
            inDegree[i] = 0
            
        # Create in-degree matrix and adj matrix based on the prereq relationships.
        for item in prerequisites:
            if item[1] not in adjList:
                adjList[item[1]] = [item[0]] 
            else: 
                adjList[item[1]].append(item[0])
            inDegree[item[0]] += 1

        q = Queue.Queue()
        result = []
        
        # Use bfs to trace out a path from the first course to the last course in the course chain.
        # We start from the node with in degree 0.
        for key in inDegree:
            if inDegree[key] == 0:
                q.put(key)
        while not q.empty():
            node = q.get()
            result.append(node)
            if node in adjList:
                for item in adjList[node]:
                    inDegree[item] -= 1
                    if inDegree[item] == 0:
                        q.put(item)
                    
        
        return result if len(result) == numCourses else []