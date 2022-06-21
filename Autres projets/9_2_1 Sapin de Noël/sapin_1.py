# afficher le sommet du sapin
print('       ^')
# afficher le triangle du feuillage
for i in range(7, 0, -1): 
    for j in range(i-1):
        print(' ', end='')
    print('/', end='') # afficher bord /
    for j in range(15-2*i):
        print(' ', end='')
    print('\\') # afficher bord \

# afficher le tronc
for i in range(0,3,1):
    for i in range(0, 6, 1):
        print(' ', end='')
    print("|||", end='') # afficher bois |||
    print()
    
