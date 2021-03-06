import re

def contains_substring(line, substring):
    return True if re.search(substring, line) else False

def process_file(fileName, words_cache, substring, replacement):
    try:
        file = open(fileName, 'r')
    except IOError:
        print "File was not found, please provide one named 'enable1.txt'"
        print "or download from: https://dotnetperls-controls.googlecode.com/files/enable1.txt"
        exit()

    while True:
        line = file.readline().strip()

        if contains_substring(line, substring):
            words_cache.add_or_replace(line)

        if not line:
            break

    file.close()

    words_cache.sort()
    words_cache.replace_and_show(substring, replacement)

    pass


class BaseClass:
    'Keeps commong code'

    def __init__(self, size, order):
        self.words = []
        self.size = size
        self.order = order

    def sort(self):
        if self.order == "DESCENDING":
            self.words.sort()
            self.words.sort(key=len, reverse=True)
        elif self.order == "ASCENDING":
            self.words.sort()
            self.words.sort(key=len, reverse=False)

    def replace_and_show(self, substring, replacement):
        for i in range(0, len(self.words)):
            print self.words[i].replace(substring, replacement), ":", self.words[i]

class LongWordsCache(BaseClass):
    'Keeps longest words containing given substring'

    def add_or_replace(self, word):
        if len(self.words) < self.size:
            self.words.append(word)
        else:
            for i in range(0, len(self.words)):
                if len(self.words[i]) < len(word):
                    self.words[i] = word
                    break
        pass


class ShortWordsCache(BaseClass):
    'Keeps shortest words containing given substring'

    def add_or_replace(self, word):
        if len(self.words) < self.size:
            self.words.append(word)
        else:
            for i in range(0, len(self.words)):
                if len(self.words[i]) > len(word):
                    self.words[i] = word
                    break
        pass


# main logic

FILE_NAME = 'enable1.txt'
CACHE_SIZE = 10
SUBSTRING = 'at'
REPLACEMENT = '@'

long_words = LongWordsCache(CACHE_SIZE, "DESCENDING")
short_words = ShortWordsCache(CACHE_SIZE, "ASCENDING")

process_file(FILE_NAME, long_words, SUBSTRING, REPLACEMENT)
process_file(FILE_NAME, short_words, SUBSTRING, REPLACEMENT)
