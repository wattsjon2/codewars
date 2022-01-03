#The birds-eye view
#^^^^^^
# ^^^^^^^^
#  ^^^^^^^
#  ^^^^^
#  ^^^^^^^^^^^
#  ^^^^^^
#  ^^^^
#The bird-brain calculations
#111111
# 1^^^^111
#  1^^^^11
#  1^^^1
#  1^^^^111111
#  1^^^11
#  1111
#111111
# 12222111
#  12^^211
#  12^21
#  12^^2111111
#  122211
#  1111
#111111
# 12222111
#  1233211
#  12321
#  12332111111
#  122211
#  1111

def peak_height(mountain):    
    stringLen = len(mountain[0])
    level = 96
    checkList = []
    nullCheck = True
    for i in range(len(mountain)):
        checkList.append(False)
        if '^' in mountain[i] and nullCheck == True:
            nullCheck = False
    
    if nullCheck == True:
        return 0

    for peak in mountain:
        if peak !=[]:
            nullCheck = False
            break
        nullCheck = True

    if nullCheck == True:
        return level

    while False in checkList:
        print(mountain)
        for i in range(len(mountain)):
            if i == 0 or i == len(mountain) - 1:
                
                birdLevel = mountain[i].replace('^',chr(level + 1))
                mountain.pop(i)
                mountain.insert(i, birdLevel)
                checkList.pop(i)
                checkList.insert(i, True)
            else:
                curString = mountain[i]
                for x in range(stringLen):              
                    if curString[x] == '^':
                        if curString[x-1] == " " and x != 0:
                            curString = curString[:x] + chr(level + 1) + curString[x + 1:]
                        
                        elif x != stringLen - 1 and curString[x+1] == " ":
                            curString = curString[:x] + chr(level + 1) + curString[x + 1:]
                        
                        elif mountain[i-1][x] == ' ' or mountain[i+1][x] == ' ':
                            curString = curString[:x] + chr(level + 1) + curString[x + 1:]
                        
                        elif curString[x-1] == chr(level) and x != 0: 
                            curString = curString[:x] + chr(level + 1) + curString[x + 1:]    
                        
                        elif x != stringLen - 1 and curString[x+1] == chr(level):
                            curString = curString[:x] + chr(level + 1) + curString[x + 1:] 

                        elif mountain[i-1][x] == chr(level) or mountain[i+1][x] == chr(level):
                            curString = curString[:x] + chr(level + 1) + curString[x + 1:]
                        
                mountain.pop(i)
                mountain.insert(i, curString)

            if checkList[i] == False:
                if '^' not in mountain[i]:
                    checkList.pop(i)
                    checkList.insert(i, True)    
            
        level += 1

    return level - 96



        




mountain = [
          "^^^^^^        ",
          " ^^^^^^^^     ",
          "  ^^^^^^^     ",
          "  ^^^^^       ",
          "  ^^^^^^^^^^^ ",
          "  ^^^^^^      ",
          "  ^^^^        "
        ]   


mountain2 = [
            "     ^^^^^^ ",
            " ^^^^^^^^   ",
            "^^^^^^^^^   ",
            "  ^^^^^^^^  ",
            "  ^^^^^^^^^ ",
            "^^^^^^^^^^^ ",
            "^^^^^^^^^^^ ",
            "  ^^^^^^^^^ ",
            "  ^^^^^^^^  ",
            "  ^^^^^^^   ",
            "  ^^^^^^    ",
            "   ^^^^^^   ",
            "    ^^^^^   ",
            "      ^^    "
        ]


mountain3 = [
            "^^   ^^^  ^^ ",
            "^ ^^  ^^^    ",
            "  ^^^   ^^   ",
            "    ^^ ^^    ",
            "   ^  ^      ",
            "    ^^       ",
            " ^^^^^^^^    ",
            "  ^^^^^^^^   ",
            " ^^ ^^^   ^^ ",
            "^^^    ^^ ^^ ",
            "     ^^^^^^^ "
]

mountainNull = ['      ', '      ', '      ']

mountain4 = [
            '^^^^^       ',
            '^^^^^       ', 
            '^^^^^       ', 
            '            ', 
            '     ^^^^^^^', 
            '     ^^^^^^^', 
            '     ^^^^^^^', 
            '     ^^^^^^^', 
            '     ^^^^^^^', 
            '     ^^^^^^^', 
            '     ^^^^^^^']


mountain5 =            ['^^^^^^^^^^^^^^^^^^^^^', '^^^^^^^^^^^^^^^^^^^^^', '^^^^^^^^^^^^^^^^^^^^^', '^^^^^^^^^^^^^^^^^^^^^', '^^^^^^^^^^^^^^^^^^^^^', '^^^^^^^^^^^^^^^^^^^^^', '^^^^^^^^^^^^^^^^^^^^^', '^^^^^^^^^^^^^^^^^^^^^', '^^^^^^^^^^^^^^^^^^^^^', '^^^^^^^^^^^^^^^^^^^^^', '^^^^^^^^^^^^^^^^^^^^^', '^^^^^^^^^^^^^^^^^^^^^', '^^^^^^^^^^^^^^^^^^^^^', '^^^^^^^^^^^^^^^^^^^^^', '^^^^^^^^^^^^^^^^^^^^^', '^^^^^^^^^^^^^^^^^^^^^', '^^^^^^^^^^^^^^^^^^^^^', '^^^^^^^^^^^^^^^^^^^^^', '^^^^^^^^^^^^^^^^^^^^^', '^^^^^^^^^^^^^^^^^^^^^', '^^^^^^^^^^^^^^^^^^^^^']

mountain6 = ['     ^^^^^^', ' ^^^^^^^^  ', '^^^^^^^^^  ', '  ^^^^^^^^ ', '  ^^^^^^^^^', '^^^^^^^^^^^', '^^^^^^^^^^^', '  ^^^^^^^^^', '  ^^^^^^^^ ', '  ^^^^^^^  ', '  ^^^^^^   ', '   ^^^^^^  ', '    ^^^^^  ', '      ^^   ']

print(peak_height(mountain6))

