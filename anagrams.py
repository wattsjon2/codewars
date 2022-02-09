#What is an anagram? Well, two words are anagrams of each other if they both contain the same letters. For example:

#'abba' & 'baab' == true

#'abba' & 'bbaa' == true

#'abba' & 'abbba' == false

#'abba' & 'abca' == false
#Write a function that will find all the anagrams of a word from a list. You will be given two inputs a word and an array with words. You should return an array of all the anagrams or an empty array if there are none. For example:

#anagrams('abba', ['aabb', 'abcd', 'bbaa', 'dada']) => ['aabb', 'bbaa']

#anagrams('racer', ['crazer', 'carer', 'racar', 'caers', 'racer']) => ['carer', 'racer']

#anagrams('laser', ['lazing', 'lazy',  'lacer']) => []

def anagrams(word, words):
    wordDict = {}
    currentDict = {}
    anagrams = []

    for letter in word:
        if letter not in wordDict:
            wordDict[letter] = 1
        else:
            wordDict[letter] += 1
    
    for current in words:
        for letter in current:
            if letter not in currentDict:
                currentDict[letter] = 1
            else:
                currentDict[letter] += 1
        if wordDict == currentDict:
            anagrams.append(current)
        currentDict = {}
    
    return anagrams



print(anagrams('abba', ['aabb', 'abcd', 'bbaa', 'dada']))
print(anagrams('racer', ['crazer', 'carer', 'racar', 'caers', 'racer']))

def anagrams2(word, words): return [item for item in words if sorted(item)==sorted(word)]