class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0
        n = len(wordList)
        visited = [False] * n
        q = deque([(beginWord, 1)])

        while q:
            cur_word, cur_step = q.popleft()
            if cur_word == endWord:
                return cur_step
            for i in range(n):
                if not visited[i] and self.check_diff_by_one(cur_word, wordList[i]):
                    visited[i] = True
                    q.append((wordList[i], cur_step+1))
        return 0

    def check_diff_by_one(self, word1: str, word2: str) -> bool:
        n = len(word1)
        count = 0
        for i in range(n):
            if word1[i] != word2[i]:
                count += 1
        return True if count == 1 else False