def triangle(num):
    if num < 2:
        return

    for i in range(num - 1):
        print((num - i) * ' ', end='')
        print('/', end='')
        print(i * 2 * ' ', end='')
        print("\\")
    
    print(' ', end='')
    print('/', end='')
    print(((i * 2) + 2) * '-', end='')
    print('\\')

triangle(6)
