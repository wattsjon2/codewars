def is_pangram(s):
    return set(string.lowercase) <= set(s.lower())

def is_pangram(s):
    s = s.lower()
    for char in 'abcdefghijklmnopqrstuvwxyz':
        if char not in s:
            return False
    return True

def is_pangram(s):
    return set(string.ascii_lowercase).issubset(s.lower())