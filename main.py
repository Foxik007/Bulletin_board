from collections import Counter


class Text:
    def __init__(self,text):
        self.text = text

    def long_word(self):
        a = self.text.split()
        b = max(a,key=len) #
        return b

    def word_count(self):
        counter = Counter(self.text.split())
        return counter.most_common()[0]



word = Text('Лето пришло🥳! Лето И оно оно оно обещает быть очень насыщенным! Ещё не решили, чем заняться этим летом в Москве? Тогда наша подборка самых интересных событий - для Вас! ')

print(word.long_word())
print(word.word_count())
