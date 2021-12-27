# put a space in camel case -> helloWorld = hello World

def age_type():
    age_input = int(input('What is your age?'))
    if age_input < 18:
        print("kids")
    elif age_input > 65:
        print("seniors")
    else:
        print("adults")


# best solution
# def solution(s):
#    return ''.join(' ' + c if c.isupper() else c for c in s)
