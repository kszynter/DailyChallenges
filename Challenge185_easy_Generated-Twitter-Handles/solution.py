import re

# DONE read file
# DONE check whether contains 'at'
# DONE save 10 longest
# DONE save 10 shortest
# TODO replace 'at' with '@'
# DONE print sorted on the screen

def contains_at(line):
    return True if re.search('at', line) else False

def process_file(fileName, words_cache):
    file = open(fileName, 'r')

    while True:
        line = file.readline().strip()

        if contains_at(line):
            words_cache.add_or_replace(line)

        if not line:
            break

    file.close()

    pass


class BaseClass:

    def __init__(self, size):
        self.size = size
        self.words = []

    def print_sorted(self, order):
        if order == "DESCENDING":
            self.words.sort()
            self.words.sort(key=len, reverse=True)
            for word in self.words:
                print word
        elif order == "ASCENDING":
            self.words.sort()
            self.words.sort(key=len, reverse=False)
            for word in self.words:
                print word


class LongWordsCache(BaseClass):
    'Keeps longest words containing \'at\''

    def add_or_replace(self, word):
        # if below max cap, then just add new word
        if len(self.words) < self.size:
            self.words.append(word)
        # else check which smalle rword we can replace
        else:
            for i in range(0, len(self.words)):
                if len(self.words[i]) < len(word):
                    self.words[i] = word
                    break
        pass

class ShortWordsCache(BaseClass):
    'Keeps shortest words containing \'at\''

    def add_or_replace(self, word):
        # if below max cap, then just add new word
        if len(self.words) < self.size:
            self.words.append(word)
        # else check which smalle rword we can replace
        else:
            for i in range(0, len(self.words)):
                if len(self.words[i]) > len(word):
                    self.words[i] = word
                    break
        pass

# main logic

CACHE_SIZE = 10
FILE_NAME = 'enable1.txt'

long_words = LongWordsCache(CACHE_SIZE)
short_words = ShortWordsCache(CACHE_SIZE)

process_file(FILE_NAME, long_words)
process_file(FILE_NAME, short_words)

long_words.print_sorted("DESCENDING")
short_words.print_sorted("ASCENDING")
