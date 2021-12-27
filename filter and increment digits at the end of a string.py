# filter the end digits out of a string, increment them by 1 and return the string with the incremented digit

# abc123 -> abc124    abc0123  -> abc0124   a2bc0129 -> a2bc0130

def increment_string(strng):
    x = 0
    z = 0

    while x < len(strng):
        if strng[x].isnumeric() == True:
            z += 1
            x += 1
        else:
            z = 0
            x += 1
    
    num_end = strng[len(strng) - z: len(strng)]
    
    if num_end == "":
        num_end = 0
        r = 1
    else:    
        r = len(num_end)              
    num_end = int(num_end) + 1
    first_part = strng[0: len(strng)-z]
    combined_str = first_part + str(num_end).zfill(r)
    return combined_str

print(increment_string("foo"))
print(increment_string("foo12"))
print(increment_string("fo1o12"))
print(increment_string("foo00"))
print(increment_string("foo09"))

# top kata

#def increment_string(strng):
#    head = strng.rstrip('0123456789')
#    tail = strng[len(head):]
#    if tail == "": return strng+"1"
#    return head + str(int(tail) + 1).zfill(len(tail))


