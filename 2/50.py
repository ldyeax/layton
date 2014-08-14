from itertools import permutations
perms = permutations([1,1,0,0,0])


for cows in perms:
    #print cows
    a = cows[0]
    b = cows[1]
    c = cows[2]
    d = cows[3]
    e = cows[4]
    
    if (not d) == a and (not c) == b and a == c and (not e) == d and (not b) == e:
        print cows

    #print a,b,c,d,e

print "done"
