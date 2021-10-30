import itertools
from collections import Counter
from typing import List


class BruteForceSolution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        if not s or not words:
            return []

        words_combinations = itertools.permutations(words)
        words_combinations = set(["".join(words) for words in words_combinations])
        result = []

        for word in words_combinations:
            start = 0
            while True:
                try:
                    start = s.index(word, start)
                    result.append(start)
                    start += 1
                except ValueError:
                    break

        return result


class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        result = []
        origin, word_len, str_len = Counter(words), len(words[0]), len(s)
        length = len(words)

        for i in range(str_len - word_len * length + 1):
            current = Counter(origin)
            exists_in_counter = True

            for j in range(i, i + word_len * length, word_len):
                if not current[s[j:j + word_len]]:
                    exists_in_counter = False
                    break
                else:
                    current[s[j:j + word_len]] -= 1

            if exists_in_counter:
                result.append(i)

        return result
