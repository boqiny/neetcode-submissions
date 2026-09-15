class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        graph = defaultdict(list)

        def connected(src, dest, visited) -> bool:
            if src == dest:
                return True
            visited.add(src)
            for nei in graph[src]:
                if nei not in visited and connected(nei, dest, visited):
                    return True
            return False
        
        for a,b in edges:
            if connected(a, b, set()):
                return [a,b]
            graph[a].append(b)
            graph[b].append(a)
        