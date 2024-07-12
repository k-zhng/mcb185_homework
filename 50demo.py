import math
seq = 'GAATTC'
print(seq[-1])
for nt in seq: print(nt, end='')
print()
for i in range(len(seq)):
    print(i, seq[i])
    
s = 'ABCDEFGHIJ'
print(s[0:5])
print(s[0:8:2])
print(s[::-1])

tax = ('Homo', 'sapiens', 9606)
print(tax)
print(tax[0])
print(tax[::-1])

def quadratic(a, b, c):
    x1 = (-b + (b**2 - 4*a*c)**0.5) / (2*a)
    x2 = (-b - (b**2 - 4*a*c)**0.5) / (2*a)
    return x1, x2
    
x1, x2 = quadratic(5, 6, 1)          # unpacked tuple - yes
print(x1, x2)                        # pretty
intercepts = quadratic(5, 6, 1)      # packed tuple - no
print(intercepts[0], intercepts[1])  # ugly

nts = 'ACGT'
for i in range(len(nts)):
    print(i, nts[i])
    
for i, nt in enumerate(nts):
    print(i, nt)

names = ('adenine', 'cytosine', 'guanine', 'thymine')
for i in range(len(names)):
    print(nts[i], names[i])
print()
for nt, name in zip(nts, names):
    print(nt, name)
print()
for i, (nt, name) in enumerate(zip(nts, names)):
    print(i, nt, name)


nts = ['A', 'T', 'C']
print(nts)
nts[2] = 'G'
print(nts)
nts.sort()
print(nts)
nts.sort(reverse=True)
print(nts)
nucleotides = nts
nucleotides.append('C')
nucleotides.sort()
print(nts, nucleotides)
print()

text = 'good day   to you'
words = text.split()
print(words)

line = '1.41,2.7,3.14'
print(line.split(','))

alph = 'ACDEFGHIKLMPQRSVW'
print(alph)
aas = list(alph)
print(aas)
s = '-'.join(aas)
print(s)

def entropy(probs):
    h = 0
    for p in probs:
        if (p != 0):
            h -= p * math.log2(p)
    return h

print(entropy([0.2, 0.3, 0.5,0]))

