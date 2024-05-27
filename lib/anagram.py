# your code goes here!
class Anagram:
    def __init__(self, word):
        self.word = ''.join(sorted(word.lower()))

    def match(self, words):
        matched_anagrams = []
        for word in words:
            sorted_word = ''.join(sorted(word.lower()))
            if sorted_word == self.word:
             matched_anagrams.append(word)
        return matched_anagrams
