#The hamming distance between a pair of numbers is the number of binary bits that differ in their binary notation.

#Example
#For a = 25, b= 87, the result should be 4

#25: 00011001
#87: 01010111
#The hamming distance between these two would be 4 ( the 2nd, 5th, 6th, 7th bit ).

def hamming_distance(a, b):
    aBin = format(a, 'b')
    bBin = format(b, 'b')

    if len(aBin) != len(bBin):
        maxLen = max(len(aBin),len(bBin))
        aBin = aBin.zfill(maxLen)
        bBin = bBin.zfill(maxLen)
    return  len([i for i in range(len(aBin)) if aBin[i] != bBin[i]])




print(hamming_distance(25,87))
print(hamming_distance(34013,702))

