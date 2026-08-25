class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = defaultdict(list)
        for a,b in prerequisites:
            graph[b].append(a)
        
        visited = [0] * numCourses
        # 0 : not visited, 1: visiting, 2: visited

        def detect_cycle(course) -> bool:
            if visited[course] == 1:
                return True
            if visited[course] == 2:
                return False
            visited[course] = 1
            for nei in graph[course]:
                if detect_cycle(nei):
                    return True
            visited[course] = 2
            return False

        
        for i in range(numCourses):
            if detect_cycle(i):
                return False
        return True
        