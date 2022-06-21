print('       *')
print('       ^')
for i in range(7, 0, -1):
    for j in range(i-1):
        print(' ', end='')
    print('/', end='')
    for j in range(15-2*i):
        print(' ', end='')
    print('\\')


for i in range(0,3,1):
    for i in range(6):
        print(' ', end='')
    print("|||", end='')
    print()
    
