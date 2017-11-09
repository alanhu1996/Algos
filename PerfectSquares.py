# Given a positive integer n, find the least number of perfect square numbers (for example, 1, 4, 9, 16, ...) which sum to n.


import Queue
class Solution(object):
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        # BFS solution.
        
        # Find all the perfect squares below or equal to n.
        perfectSquares = []
        for i in range(n + 1):
            if i * i > n:
                break
            if i * i == n:
                return 1
            
            perfectSquares.append(i * i)
        q = Queue.Queue()
        head = 0
        q.put(head)
        visited = {}
        depth = 0
        while not q.empty():
            depth += 1
            for i in range(q.qsize()):
                node = q.get()
                # Avoid visiting a node more than once.
                if node in visited:
                    continue
                else:
                    visited[node] = True
                for p in perfectSquares:
                    if p + node < n:
                        q.put(p + node)
                    elif p + node == n:
                        return depth
        return -1