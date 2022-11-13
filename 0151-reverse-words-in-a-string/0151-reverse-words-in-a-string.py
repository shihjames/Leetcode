class Solution:
    def reverseWords(self, s: str) -> str:
        
        words = s.split(" ")
        print(words)
        new_words = []
        for word in words[::-1]:
            if word != "":
                new_words.append(word)
        
        return " ".join(new_words)