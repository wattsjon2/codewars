# single occurance = (, multiple occurances = )

def duplicate_encode(word):
    word = word.lower()
    left_curly_bracket = word.count("(")
    right_curly_bracket = word.count(")")
    if left_curly_bracket > 1 and right_curly_bracket == 1:
        right_curly_bracket_find = word.find(")")
        word = word.replace("(",")")
        word = word[:right_curly_bracket_find] +"(" + word[right_curly_bracket_find + 1:]
    elif left_curly_bracket > 1:
        word = word.replace("(",")")
    elif right_curly_bracket == 1:
        word = word.replace(")","(")

    i = 0
    while i < len(word):
        if word[i] == "(" or word[i] == ")":
            pass
        elif word.count(word[i]) > 1:
           word = word.replace(word[i], ")")
        else:
            word = word.replace(word[i], "(")
        i += 1
    return(word)

print(duplicate_encode("Success"))


#def duplicate_encode(word):
#    return "".join(["(" if word.lower().count(c) == 1 else ")" for c in word.lower()])





#    word = word.upper()
#    result = ""
#    for char in word:
#        if word.count(char) > 1:
#            result += ")"
#        else:
#            result += "("
#            
#    return result