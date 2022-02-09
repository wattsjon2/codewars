# Given a positive integer n: 0 < n < 1e6, remove the last digit until you're left with a number that is a multiple of three.

#Return n if the input is already a multiple of three, and return None if no such number exists.

#Examples

#1 => None

#25 => None

#36 => 36

#1244 => 12

# 952406 => 9

def prev_mult_of_three(n):
    while n != '':
        if int(n) % 3 == 0:
            return int(n)
        else:
            n = (str(n)[:-1])    
    return None

print(prev_mult_of_three(1))
print(prev_mult_of_three(25))
print(prev_mult_of_three(36))
print(prev_mult_of_three(1244))
print(prev_mult_of_three(952406))
