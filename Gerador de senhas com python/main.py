from random import randint
 
lista1 = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
lista2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
lista3 = ['#', '@', '$', '%', '/', '&', '!']
print(f'A senha gerada foi: {lista1[randint(0, 25)]}{lista2[randint(0, 19)]}{lista3[randint(0, 6)]}{lista2[randint(0, 9)]}{lista1[randint(0, 25)]}{lista2[randint(0, 9)]}{lista3[randint(0, 6)]}{lista1[randint(0, 25)]}')
