from random import choice


class Word:
    array_words = []
    f = open('eng_easy')

    def __init__(self):
        for i in self.f.read().splitlines():
            list_iter_data = i.split('-')
            data = (list_iter_data[0], list_iter_data[1])
            self.array_words.append(data)

    def select_random_word(self):
        return choice(self.array_words)
