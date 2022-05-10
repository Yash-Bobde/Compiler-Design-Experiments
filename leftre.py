n = int(input('Enter the number of production rules:\t'))

inp = []
print('Enter the production rules:')
for _ in range(n):
    str = input()
    inp.append(str)

print('\nThe new production rules are: ')
for str in inp:
    left, _, right = str.partition('->')
    left = left.strip()
    right = right.strip()

    alpha = []
    beta = []
    for w in right.split('|'): 
        lindx = 0
        while len(w) > lindx and len(left) > lindx and w[lindx] == left[lindx]:
            lindx += 1
        if lindx != 0:
            alpha.append(w[lindx:])
        else:
            beta.append(w)

    first = '|'.join([w + left + "'" for w in beta])
    second = '|'.join([w + left + "'" for w in alpha] + ['epsilon'])
    
    if len(alpha) != 0:
        print(left, '->', first)
        print(left + "'", '->', second)
    else:
        print(left, '->', right)