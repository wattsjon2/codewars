#pig latin translator

def pig_it(text):
    split = text.split()
    pig_latin = ""
    for word in split:
        if word in ('!', "," ,"\'" ,";" ,"\"", ".", "-" ,"?"):
            pig_latin += word
        else:
            pig_latin += (word[1:] + word[0] + "ay" + " ")
    return(pig_latin.strip()) 
    

print(pig_it("a big bear ?"))

#def pig_it(text):
#    lst = text.split()
#    return ' '.join( [word[1:] + word[:1] + 'ay' if word.isalpha() else word for word in lst])