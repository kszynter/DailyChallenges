# definitions

def strip_chars(inputString):
    WANTED = '*'
    
    guardCnt = 1
    while (True):
        try:
            index = inputString.rindex(WANTED)
        except ValueError:
            break

        inputString = remove_chars(inputString, index)
       
        guardCnt += 1
        if (guardCnt == 3):
            break

    return inputString 

def remove_chars(inputString, index):
    # char at the end
    if (is_last_char(inputString, index)):
        inputString = remove_last(inputString)
        if (len(inputString) > 0):
            inputString = remove_last(inputString)

    # char at the beginning
    if (is_first_char(inputString, index)):
        inputString = remove_first(inputString)
        if (len(inputString) > 0):
            inputString = remove_first(inputString)

    # char is in the middle 
    if (is_middle_char(inputString, index)):
        inputString = remove_at(inputString, index+1)
        inputString = remove_at(inputString, index)
        inputString = remove_at(inputString, index-1)

    return inputString

def is_first_char(inputString, index):
    return index == 0

def is_last_char(inputString, index):
    return (index == len(inputString)-1)

def is_middle_char(inputString, index):
    return (index > 0 and index < len(inputString)-1)

def remove_last(inputString):
    return inputString[0:len(inputString)-1]

def remove_first(inputString):
    return inputString[1:len(inputString)]

def remove_at(inputString, index):
    # print "inp: ", inputString, " (", index, ")"
    # print "ret: ", inputString[0:index] + "_" + inputString[index+1:len(inputString)]
    return inputString[0:index] + inputString[index+1:len(inputString)]

def show_result_message(inputString, output, expected):
    print "-------------------------"
    print OKGREEN+"PASS"+ENDC if output == expected else FAIL+"FAIL"+ENDC,
    print "input:", "'"+inputString+"'", 
    print "output:", "'"+output+"'", 
    print "expected:", "'"+expected+"'"

# main logic

OKGREEN = '\033[92m'
FAIL = '\033[91m'
ENDC = '\033[0m'

inputs = ["adf*lp", "a*o", "*dech*", "de**po", "sa*n*ti", "abc"]
expecteds = ["adp", "", "ec", "do", "si", "abc"]

for i in range(0, len(inputs)):
    output = strip_chars(inputs[i])
    show_result_message(inputs[i], output, expecteds[i])
