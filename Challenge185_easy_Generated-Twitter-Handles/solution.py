import re

# DONE read file
# DONE check whether contains 'at'
# TODO save 10 longest
# TODO save 10 shortest
# TODO replace 'at' with '@'
# TODO print sorted on the screen

def contains_at(line):
    return True if re.search('at', line) else False

def process_file(fileName):
    file = open(fileName, 'r')

    counter = 0
    while True:
        line = file.readline()

        if contains_at(line):
            counter += 1

        if not line:
            break

    file.close()

    print "Words with 'at':", counter
    pass

# main logic

process_file('enable1.txt')
