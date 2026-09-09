class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        graph = defaultdict(list[int])
        for a,b in edges:
            graph[b].append(a)
            graph[a].append(b)

        visited = defaultdict(int)

        def dfs(node, parent) -> bool: # detect cycle
            if visited[node] == 1:
                return True
            if visited[node] == 2:
                return False
            visited[node] = 1
            for nei in graph[node]:
                if nei != parent:
                    if dfs(nei, node):
                        return True
            visited[node] = 2
            return False
        
        return not dfs(0, -1) and len(visited) == n
        
