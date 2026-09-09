class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        graph = defaultdict(list)
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)

        visited = set()

        def dfs(node, parent) -> bool:   # True = 有环
            if node in visited:
                return True
            visited.add(node)
            for nei in graph[node]:
                if nei != parent and dfs(nei, node):
                    return True
            return False

        return not dfs(0, -1) and len(visited) == n