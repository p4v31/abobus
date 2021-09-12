def convert(number):
    """В возврящаемую строку дописываются:
'Pling', если число number делится на 3,
'Plang', если число number делится на 5,
'Plong', если число number делится на 7,
само число number, если оно не делится ни на 3, ни на 5, ни на 7."""
    a=int(input())
    if a%3==0:
        print('Pling')
    elif a%5==0:
        print('Pling')
    elif a%7==0:
        print('Pling')
    elif a%3!=0 and a%5!=0 and a%7!=0:
        print(a)
    return str(number) # эту строку можно удалить
