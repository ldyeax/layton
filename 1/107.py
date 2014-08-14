from copy import deepcopy

grid =  [ [1, 2, 3], [4, 8, 7], [6, 0, 1] ]
target =[ [1, 2, 3], [4, 0, 6], [7, 8, 1] ]
from random import shuffle

used_states = []

def up(a, y, x):
	arr = deepcopy(a)
	arr[y - 1][x] = arr[y][x]
	arr[y][x] = 0
	return arr
def dn(a, y, x):
	arr = deepcopy(a)
	arr[y + 1][x] = arr[y][x]
	arr[y][x] = 0
	return arr
def le(a, y, x):
	arr = deepcopy(a)
	arr[y][x - 1] = arr[y][x]
	arr[y][x] = 0
	return arr
def ri(a, y, x):
	arr = deepcopy(a)
	arr[y][x + 1] = arr[y][x]
	arr[y][x] = 0
	return arr

import sys
lim = int(sys.argv[1])

cnt = 0
def go(arr, n = lim, history = [], last = []):
	global cnt

	if arr in used_states:
		return
	used_states.append(arr)

	if last != []:
		history.append(last)
	
	#print " " * n, history

	#for row in arr:
	#	print " " * (lim - n), row
	#raw_input()
	
	if n <= 0:
		return
	if arr == target:
		print "found:",cnt
		for move in history:
			print move.__name__
		print "==="
		return
	cnt += 1
	for y in range(3):
		for x in range(3):
			if arr[y][x] == 0:
				def one():
					if y < 2 and last != dn:
						go(up(arr, y + 1, x), n - 1, history, up)
				def two():
					if y > 0 and last != [up, y + 1, x]:
						go(dn(arr, y - 1, x), n - 1, history, dn)
				def three():
					if x > 0 and last != [le, y, x + 1]:
						go(ri(arr, y, x - 1), n - 1, history, ri)
				def four():
					if x < 2 and last != [ri, y, x - 1]:
						go(le(arr, y, x + 1), n - 1, history, le)
				funcs = [one,two,three,four]
				shuffle(funcs)
				for f in funcs:
					f()


go(grid)
print cnt
