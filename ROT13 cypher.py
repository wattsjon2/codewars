# make a chipher that changes a letter 13 letters to the right

def rot13(message):
    index = 0
    new_message = ""
    while index < len(message):
        ascii_num = ord(message[index])
        if ascii_num >= 65 and ascii_num <= 90:
            ascii_num += 13
            if ascii_num > 90:
                ascii_num = ascii_num - 91 + 65
        elif ascii_num >= 97 and ascii_num <= 122:
            ascii_num += 13
            if ascii_num > 122:
                ascii_num = ascii_num - 123 + 97
        new_message += chr(ascii_num)
        index += 1
    return(new_message)

print(rot13("abc"))

# best solutions

#import string
#from codecs import encode as _dont_use_this_
#from string import maketrans, lowercase, uppercase

#def rot13(message):
#    lower = maketrans(lowercase, lowercase[13:] + lowercase[:13])
#    upper = maketrans(uppercase, uppercase[13:] + uppercase[:13])
#    return message.translate(lower).translate(upper)

