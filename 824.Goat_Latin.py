vowels = ["a", "e", "i", "o", "u"]


class Solution:
    def toGoatLatin(self, sentence: str) -> str:
        words = sentence.split(" ")
        print(words)
        for i, word in enumerate(words):
            print(word)
            if word[0].lower() in vowels:
                words[i] += "ma"
            else:
                words[i] = word[1:] + word[0] + "ma"
            words[i] += "a" * (i+1)

        print(words)
        sentence = ""
        for word in words:
            sentence += word + " "

        return sentence[:-1]