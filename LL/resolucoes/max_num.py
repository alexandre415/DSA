list = [1,20,10,40]
print(f'Usando a funcao max {max(list)}')
max = list[0]

#or

for i in list:
    if i > max:
        max = i

print(max)
