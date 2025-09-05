'''
Zatražite od korisnika unos dva broja. 
Nakon unosa brojeva, ispišite:
    zbroj, razliku, umnožak, količnik (rezultat djeljnja), 
    potenciranje te modulo unesenih brojeva

Svaka operacija treba biti ispisana u novom redu, a ispis treba imati uključene brojeve, 
znak računske operacije te rezultat.
PRIMJER ISPISA: 
5 + 8 = 13
5 - 8 = -3

NAPOMENA Za sada kod unosa neka kod prvog unosa drugi broj NE bude 0 (nula), 
jer nije dopušteno dijeliti s nulom. To svakako pokušajte napraviti, ali NE u prvom pokušaju.
'''

a = input('Upisite prvi broj: ')
b = input('Upisite drugi broj: ')


# print('Vrijednost a:', a)
# print('Vrijednost b:', b)

print('Zbroj brojeva a', a, 'i b', b, 'je', a + b)
print('Razlika brojeva a', a, 'i b', b, 'je', a - b)
print('Umnozak brojeva a', a, 'i b', b, 'je', a * b)
print('Kolicnik brojeva a', a, 'i b', b, 'je', a / b)
print('Potencija brojeva a', a, 'i b', b, 'je', a ** b)
print('Modula brojeva a', a, 'i b', b, 'je', a % b)
