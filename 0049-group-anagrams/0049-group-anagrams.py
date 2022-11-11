class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        word_dict = defaultdict(list)
        
        for s in strs:
            chars = [0] * 26
            for i in range(len(s)):
                chars[ord(s[i]) - ord("a")] += 1
            word_dict[tuple(chars)].append(s)
        
        return [words for chars, words in word_dict.items()]