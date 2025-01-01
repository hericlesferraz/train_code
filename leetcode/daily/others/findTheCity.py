from typing import List
from collections import deque

class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        self.distance = distanceThreshold
        return self.bfs(start=0, graph=edges)

    def bfs(self, start, graph):
            queue = deque([start])
            visited = set([start])
            distance = 0
            count_cities = 0
            i = 0
            while queue:
                node = queue.popleft()
                print('node:', node, i)
                _, _, d = graph[i]
                distance += d
                for neighbor in graph[node]:
                    print(neighbor)
                    if neighbor not in visited and self.distance > distance:
                        visited.add(neighbor)
                        queue.append(neighbor)
                        print(visited)
                        distance = 0
                        count_cities += 1
                i+= 1
            return count_cities
    
Solution().findTheCity(n=4, edges=[[0,1,3],[1,2,1],[1,3,4],[2,3,1]], distanceThreshold=40)
Solution().findTheCity(n=5, edges=[[0,1,2],[0,4,8],[1,2,3],[1,4,2],[2,3,1],[3,4,1]], distanceThreshold=2)
Solution().findTheCity(n=6, edges=[[0,3,7],[2,4,1],[0,1,5],[2,3,10],[1,3,6],[1,2,1]], distanceThreshold=417)
