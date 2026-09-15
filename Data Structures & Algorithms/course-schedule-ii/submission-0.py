class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = defaultdict(list[int])
        for a, b in prerequisites:
            graph[b].append(a)
        
        visited = [0] * numCourses
        res = []

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
            res.append(i)
            return False

        for i in range(numCourses):
            if dfs(i):
                return []
        return res[::-1]