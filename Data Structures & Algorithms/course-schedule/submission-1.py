class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = defaultdict(list)
        for a,b in prerequisites:
            graph[b].append(a)

        state = [0] * numCourses 
        # 0: unvisited, 1: visiting, 2: visited

        def dfs(course) -> bool:
            if state[course] == 1:
                return True
            if state[course] == 2:
                return False

            state[course] = 1
            for nei in graph[course]:
                if dfs(nei):
                    return True
            state[course] = 2

            return False
        
        for i in range(numCourses):
            if dfs(i):
                return False
        return True

