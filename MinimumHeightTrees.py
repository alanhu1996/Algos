# For a undirected graph with tree characteristics, we can choose any node as the root. The result graph is then a rooted tree. Among all possible rooted trees, those with minimum height are called minimum height trees (MHTs). Given such a graph, write a function to find all the MHTs and return a list of their root labels.


class Solution(object):
    def findMinHeightTrees(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        
        if n == 1:
            return [0]
        # Create non directed adj list.
        adjList = [set() for i in range(n)]
        
        for edge in edges:
            adjList[edge[1]].add(edge[0])
            adjList[edge[0]].add(edge[1])
        
        leaves = [i for i in range(n) if len(adjList[i]) == 1]
        while n > 2:
            newLeaves = []
            for leave in leaves:
                # This is the node that is neighbor to the leave node.
                adjNode = adjList[leave].pop()
                adjList[adjNode].remove(leave)
                if len(adjList[adjNode]) == 1:
                    newLeaves.append(adjNode)
                n -= 1
            leaves = newLeaves
        return leaves