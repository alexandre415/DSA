vowel = ['a', 'e', 'i', 'o', 'u']
word = "alexandre cardoso" 
count = 0
for cara in word:
    if cara in vowel:
        count +=1
count1 = 0
for cara in word:
    if cara not in vowel:
        count1 +=1 
print(f'Vowels: {count}')
print((f'Consonants: {count1}'))