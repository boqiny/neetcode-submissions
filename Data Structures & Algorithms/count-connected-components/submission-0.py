class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        visited = set()
        graph = defaultdict(list)
        for a,b in edges:
            graph[a].append(b)
            graph[b].append(a)
        
        def dfs(node, parent) -> None:
            if node in visited:
                return
            visited.add(node)
            for nei in graph[node]:
                if nei != parent:
                    dfs(nei, node)
        count = 0
        for i in range(n):
            if i not in visited:
                count += 1
                dfs(i, -1)
        return count