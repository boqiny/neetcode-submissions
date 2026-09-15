class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = defaultdict(list[int])
        for a, b in prerequisites:
            graph[b].append(a)
        
        visited = [0] * numCourses

        def dfs(i) -> bool: # return True if exist cycle
            if visited[i] == 1:
                return True
            if visited[i] == 2:
                return False
            visited[i] = 1
            for nei in graph[i]:
                if dfs(nei):
                    return True
            visited[i] = 2
            return False
        
        for i in range(numCourses):
            if dfs(i):
                return False
        return True
            
            
