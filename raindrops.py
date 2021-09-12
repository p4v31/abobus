def convert(number):
    t=False
    if number%3==0 and t==False:
        return('Pling')
        t=True
    elif number%5==0 and t==False:
        return('Plang')
        t = True
    elif number%7==0 and t==False:
        return('Plong')
        t=True
    elif number%3!=0 and number%5!=0 and number%7!=0 and t==False:
        return(int(number))
        t=True
