#Shift reduce parsing
from collections import defaultdict

n = int(input('Enter the number of production rules: '))

memo = defaultdict(list)

start_symbol = ''
print('Enter the production rules:')
for i in range(n):
    inp = input()
    left, _, right = inp.partition('->')
    left = left.strip()
    right = right.strip()
    lexemes = right.split('|')
    if i == 0:
        start_symbol = left
    for c in lexemes:
        memo[left].append(c)
     

inp = input('Enter the input string: ')
inp = inp + '$'
i = 0
s = '$'
print(f'{"Stack Contents": <15}'+" | "+f'{"Input Buffer": <15}'+ " | "+f'Parsing Action')
accepted = True
action = ''
while i<len(inp)-1 or len(s) != 2:
    action = ''
    found = False
    for key, values in memo.items():
        for value in values:
            if len(value) <= len(s) and value == s[(len(s)-len(value)):]:
                action = 'Reduce ' + key + ' -> ' + value
                print(f'{s: <15}'+" | "+f'{inp[i:]: <15}'+ " | "+f'{action}')
                s = s[:-len(value)]
                s = s + key
                found = True

    if not found and i<len(inp):
        action = 'Shift'
        print(f'{s: <15}'+" | "+f'{inp[i:]: <15}'+ " | "+f'{action}')
        s = s + inp[i]
        i += 1
    
    if action == '':
        accepted = False
        break

if accepted:
    print(f'{s: <15}'+" | "+f'{inp[i:1]: <15}'+ " | "+f'Accepted')
else:
    print(f'{s: <15}'+" | "+f'{inp[i:]: <15}'+ " | "+f'Rejected')

