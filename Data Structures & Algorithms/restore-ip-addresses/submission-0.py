class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        n = len(s)
        res = []

        def dfs(start: int, path: list[str]):
            if start == n and len(path) == 4:
                res.append(".".join(path))
            if start == n or len(path) == 4:
                return
            if 0 <= int(s[start]) <= 255:
                dfs(start+1, path + [s[start]])
            if not s[start] == '0':
                if start + 2 <= n and 0 <= int(s[start:start+2]) <= 255:
                    dfs(start+2, path + [s[start:start+2]])
                if start + 3 <= n and 0 <= int(s[start:start+3]) <= 255:
                    dfs(start+3, path + [s[start:start+3]])

        dfs(0, [])
        return res


