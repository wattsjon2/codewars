# put a space in camel case -> helloWorld = hello World

def solution(s):
    index = 1
    new_s = s[0]
    while index < len(s):
        if s[index].isupper() == True:
            new_s += " " + s[index]
        else:
            new_s += s[index]
        index += 1    
    return(new_s) 
print(solution("helloWorld"))       
