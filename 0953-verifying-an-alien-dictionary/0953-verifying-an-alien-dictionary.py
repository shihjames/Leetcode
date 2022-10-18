class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        word_dict = {}
        for index, char in enumerate(order):
            word_dict[char] = index
            
        for i in range(len(words)-1):
            for j in range(len(words[i])):
                if j >= len(words[i + 1]):
                    return False
                if word_dict[words[i][j]] > word_dict[words[i+1][j]]:
                    return False
                elif word_dict[words[i][j]] < word_dict[words[i+1][j]]:
                    break
        return True
            