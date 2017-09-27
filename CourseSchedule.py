# There are a total of n courses you have to take, labeled from 0 to n - 1.

# Some courses may have prerequisites, for example to take course 0 you have to first # take course 1, which is expressed as a pair: [0,1]

#Given the total number of courses and a list of prerequisite pairs, is it possible for you to finish all courses?

# This solution can be optimized. 

# The idea is to remove all nodes with in-degree 0 along with its neighbors iteratively. 

import Queue
 

class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        
        # Creating adjacency list.
        adjList = {}
        inDegree = {}
        for node in prerequisites:
            if node[1] not in adjList:
                adjList[node[1]] = [node[0]]
            else:
                adjList[node[1]].append(node[0])
            if node[0] not in adjList:
                adjList[node[0]] = []
                
            if node[0] not in inDegree:
                inDegree[node[0]] = 1
            else:
                inDegree[node[0]] += 1
                
            if node[1] not in inDegree:
                inDegree[node[1]] = 0
        print(inDegree) 
        print(adjList)
        for i in range(len(inDegree)):
            tmp = -1
            for s in inDegree:
                if inDegree[s] == 0:
                    tmp = s
                    break
            if(tmp == -1):
                return False
            inDegree[tmp] = -1
            for child in adjList[tmp]:
                inDegree[child] -= 1
            tmp = - 1
                    
        
        return True