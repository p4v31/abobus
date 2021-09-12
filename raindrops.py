def convert(number):
    a=[]
    if number%3==0:
        a.append('Pling')
    if number%5==0:
        a.append('Plang')
    if number%7==0:
        a.append('Plong')
    if number%3!=0 and number%5!=0 and number%7!=0:
        a.append(str(number))
    b=str(''.join(a))
    return(b)
#
