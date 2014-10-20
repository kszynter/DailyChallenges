import re

def show_result_message(inputString, output, expected):
    print "-------------------------"
    print OKGREEN+"PASS"+ENDC if output == expected else FAIL+"FAIL"+ENDC,
    print "input:", "'"+inputString+"'", 
    print "output:", "'"+output+"'", 
    print "expected:", "'"+expected+"'"

def strip_chars(inputString):
    # re.sub(pattern, repl, string, max=0)
    return re.sub('.{0,1}\*+.{0,1}', '', inputString)

# main logic

OKGREEN = '\033[92m'
FAIL = '\033[91m'
ENDC = '\033[0m'

inputs = ["adf*lp", "a*o", "*dech*", "de**po", "sa*n*ti", "abc"]
expecteds = ["adp", "", "ec", "do", "si", "abc"]

for i in range(0, len(inputs)):
    output = strip_chars(inputs[i])
    show_result_message(inputs[i], output, expecteds[i])

