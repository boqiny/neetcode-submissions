class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        rank = {}
        for i, c in enumerate(order):
            rank[c] = i

        def in_order(a: str, b: str) -> bool:
            for i in range(min(len(a), len(b))):
                ord_ai = rank[a[i]]
                ord_bi = rank[b[i]]
                if ord_ai < ord_bi:
                    return True
                if ord_ai > ord_bi:
                    return False
            return len(a) <= len(b)
        
        for i in range(len(words) - 1):
            if not in_order(words[i], words[i+1]):
                return False
        return True