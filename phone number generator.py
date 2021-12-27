#Create a phone number given a list of 10 digits

def create_phone_number(n):
    phone_Number = "("
    
    for i in n:
        if len(phone_Number) == 4:
            phone_Number += ") "
        if len(phone_Number) == 9:
            phone_Number += "-"
        phone_Number += str(i)
    return(phone_Number)
        
print(create_phone_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]))

#def create_phone_number(n):
#    return "({}{}{}) {}{}{}-{}{}{}{}".format(*n)

#def create_phone_number(n):
#    n = ''.join(map(str,n))
#    return '(%s) %s-%s'%(n[:3], n[3:6], n[6:])