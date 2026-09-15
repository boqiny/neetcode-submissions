class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        visited = set()
        graph = defaultdict(list)
        for a,b in edges:
            graph[a].append(b)
            graph[b].append(a)
        
        def dfs(node) -> None:
            visited.add(node)
            for nei in graph[node]:
                if nei not in visited:
                    dfs(nei)

        count = 0
        for i in range(n):
            if i not in visited:
                count += 1
                dfs(i)
        return count