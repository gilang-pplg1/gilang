A = int(input('Masukkan Nilai A             = '))
B = int(input('Masukkan Nilai B             = '))
op = input('Masukkan operator (+, -, /, *) = ')
if op == '+':
    result = A + B
    print(f'Hasil: {A} + {B} = {result}')
elif op == '-':
    result = A - B
    print(f'Hasil: {A} - {B} = {result}')
elif op == '*':
    result = A * B
    print(f'Hasil: {A} * {B} = {result}')
elif op == '/':
    if B != 0:
        result = A / B
        print(f'Hasil: {A} / {B} = {result}') 
    else:
        print("Tidak bisa di bagi dengan nol")
else:
    print("Operator tidak valid, silakan gunakan operator yang lain")