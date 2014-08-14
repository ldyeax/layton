from itertools import permutations

perms = list(permutations([n for n in xrange(1,10)]))

print perms[0]

print [n for n in perms if n[0]*n[1]*n[2] == n[1]*n[3]*n[4] and n[1]*n[3]*n[4] == n[5]*n[4]*n[6]]
