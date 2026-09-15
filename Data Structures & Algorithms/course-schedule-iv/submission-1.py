class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        graph = defaultdict(list)
        for a,b in prerequisites:
            graph[a].append(b)
        
        def dfs(i, target, visited) -> bool:
            if i == target:
                return True
            visited.add(i)
            for nei in graph[i]:
                if nei not in visited and dfs(nei, target, visited):
                    return True
            return False

        res = []
        for a,b in queries:
            if dfs(a, b, set()):
                res.append(True)
            else:
                res.append(False)
        return res
