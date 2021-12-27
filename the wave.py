# make a string do the wave in a list eg: "abc d" =[:Abc d, aBc d, abC d, abc D]

def wave(people):
    index = 0
    wave =[]
    while index < len(people):
        replace = people[index].capitalize()
        if replace != " ":
            wave_word = people[:index] + replace + people[index + 1:]
            index += 1
            wave.append(wave_word)
        else:
            index += 1
    return(wave)

print(wave("ab c"))

#best soultion
#def wave(str):
#    return [str[:i] + str[i].upper() + str[i+1:] for i in range(len(str)) if str[i].isalpha()]