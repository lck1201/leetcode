# wrong
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: 'List[str]') -> 'int':
        dict = set(wordList)
        todo = list()
        todo.append(beginWord)
        ladder = 1
        while todo:
            n = len(todo)
            for i in range(n):
                word = todo.pop(0)
                if word == endWord:
                    return ladder
                dict -= {word}

                word = word.split()
                for j in range(len(word)):
                    c = word[j]
                    for k in range(0, 26):
                        word[j] = chr(97 + k)
                        NewWord = ''.join(word)
                        if NewWord in dict and NewWord:
                            todo.append(word)
                    word[j] = c
            ladder += 1

        return 0


bw = 'hit'
ew = 'cog'
wl = ["hot", "dot", "dog", "lot", "log", "cog"]
Solution().ladderLength(bw, ew, wl)
