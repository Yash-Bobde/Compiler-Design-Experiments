
from collections import defaultdict
import string

str = input('Enter the production rule: \n')

def find_pref(lexemes):
    if not lexemes:
        return ''
    all_match = 0
    comm_pref = ''
    for k in range(len(max(lexemes, key=len))):
        max_match = 0
        pref = ''
        d = defaultdict(lambda: 0)
        for i in lexemes:
            if len(i) > k and (k == 0 or (k > 0 and i[k-1] == comm_pref[k-1])):
                d[i[k]] += 1
                max_match = max(d[i[k]], max_match)
        if all_match <= max_match and max_match != 1:
            for key, val in d.items():
                if val == max_match:
                    pref = key
                    break
            all_match = max_match
            comm_pref = comm_pref + pref
        else:
            return comm_pref
        
    return comm_pref
                                

print('\nThe new production rules are: ')
left, _, right = str.partition('->')
left = left.strip()
right = right.strip()

alpha = []
beta = []
lexemes = right.split('|')

alpha = []
beta = []
used = []
epsilon = False

used = set(left)
for l in lexemes:
    for w in list(l):
        used.add(w)

while (prefix := find_pref(lexemes)) != '':
    beta = []
    alpha = []
    alpha_eps = epsilon
    if len(left) > 1:
        for c in string.ascii_uppercase:
            if c not in used:
                a = c
                used.add(a)
                break

    else:
        a = left + "'"
    used.add(a)
    alpha.append(prefix + a)
    for l in lexemes:
        if len(prefix) <= len(l) and prefix == l[:len(prefix)]:
            rem = l[len(prefix):]
            if len(rem) == 0:
                epsilon = True
            else:
                beta.append(rem)
        else:
            alpha.append(l)
    lexemes = beta
    if alpha_eps:
        alpha.append('epsilon')
    alpha_str = '|'.join(alpha)
    print(left, '->', alpha_str)
    left = a

if not beta:
    print(left, '->', right)
else:
    if epsilon:
        beta.append('epsilon')
    beta_str = '|'.join(beta)
    print(left, '->', beta_str)
        
    


   