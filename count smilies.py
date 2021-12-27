# count the smiley faces 

def count_smileys(arr):
    return arr.count(":D") + arr.count(";D") + arr.count(":)") + arr.count(";)") + arr.count(":-D") + arr.count(";-D") + arr.count(":-)") + arr.count(";-)") + arr.count(":~D") + arr.count(":~D") + arr.count(":~)") + arr.count(":~)")


print(count_smileys([":","D",":D",":-D"]))