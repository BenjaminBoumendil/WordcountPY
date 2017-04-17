import sys
from collections import Counter
from itertools import chain

class WordCount:
    """
    WordCount class count words and occurrences in files
    """
    words_dict = Counter()
    total_words = 0

    def __init__(self, dictfile):
        self.read_dictfile(dictfile)

    def read_file(self, filename):
        """
        Read 'filename' and return a Counter of all words in it
        """
        with open(filename, 'r') as f:
            return Counter(chain.from_iterable(map(str.split, f)))

    def read_dictfile(self, filename):
        """
        Read 'filename' and Build 'self.words_dict' with words to count
        """
        with open(filename, 'r') as f:
            for line in map(str.strip, f):
                if line.strip() and line[0] != '#' and line.count(" ") == 0:
                    self.words_dict[line] = 0

    def print_result(self):
        """
        Print 'self.words_dict' and 'self.total_words'
        """
        for key, value in self.words_dict.items():
            print("{}\t{}".format(value, key))
        print("{}\tTotal Words".format(self.total_words))

    def count(self, inputfile_list):
        """
        Count all words and occurrences from 'self.words_dict'
        in 'inputfile_list' and print the result
        """
        for inputfile in inputfile_list:
            for key, value in self.read_file(inputfile).items():
                if key:
                    self.total_words += value
                if key in self.words_dict:
                    self.words_dict[key] += value

        self.print_result()

def main():
    if (len(sys.argv) < 3):
        print("Error: missing arguments")
        return -1

    wordcount = WordCount(sys.argv[1])

    wordcount.count(sys.argv[2:])

    return 0

if __name__ == '__main__':
    main()
