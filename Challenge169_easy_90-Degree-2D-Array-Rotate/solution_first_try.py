from numpy import *

# definitions

def rotate_clockwise(arr):
    rowLen = len(arr[0])
    colLen = len(arr)
    # print 'lens: ', str(rowLen) + ':' + str(colLen)

    if (rowLen <> colLen):
        raise ValueError

    arr = arr.T
    result = zeros((rowLen,colLen))
    for r in range(0,rowLen):
        for c in range(0,colLen):
            result[r,c] = arr[r,rowLen-1-c]
    return result

def process_rotation(arr):
    print 'original'
    print arr
    print 'rotated 1x'
    r1 = rotate_clockwise(arr)
    print r1
    print 'rotated 2x'
    r1 = rotate_clockwise(r1)
    print r1
    print 'rotated 3x'
    r1 = rotate_clockwise(r1)
    print r1
    pass

# main logic

m3 = array([[1,2,3],
             [4,5,6],
             [7,8,9]])

m10 = array([[1,2,3,4,5,6,7,8,9,0],
   			  [0,9,8,7,6,5,4,3,2,1],
   			  [1,3,5,7,9,2,4,6,8,0],
   			  [0,8,6,4,2,9,7,5,3,1],
   			  [0,1,2,3,4,5,4,3,2,1],
   			  [9,8,7,6,5,6,7,8,9,0],
   			  [1,1,1,1,1,1,1,1,1,1],
   			  [2,2,2,2,2,2,2,2,2,2],
   			  [9,8,7,6,7,8,9,8,7,6],
   			  [0,0,0,0,0,0,0,0,0,0]])

process_rotation(m3)
process_rotation(m10)
