from copy import deepcopy

target = [ [1, 2, 3], [4, 8, 7], [6, 0, 9] ]
grid   = [ [1, 2, 3], [4, 0, 6], [7, 8, 9] ]
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

def go(arr, n = 20, history = "", last = []):
	#if arr in used_states:
	#	return
	#used_states.append(arr)

	if last != []:
		history += str(last) + " "
	
	#print " " * n, history

	#for row in arr:
	#	print " " * (30 - n), row
	#raw_input()
	
	if n <= 0:
		return
	if arr == target:
		print history
		return
	for y in range(3):
		for x in range(3):
			if arr[y][x] == 0:
				def one():
					if y < 2 and last != [dn, y - 1, x]:
						go(up(arr, y + 1, x), n - 1, history, [up.__name__, y + 1, x])
				def two():
					if y > 0 and last != [up, y + 1, x]:
						go(dn(arr, y - 1, x), n - 1, history, [dn.__name__, y - 1, x])
				def three():
					if x > 0 and last != [le, y, x + 1]:
						go(ri(arr, y, x - 1), n - 1, history, [ri.__name__, y, x - 1])
				def four():
					if x < 2 and last != [ri, y, x - 1]:
						go(le(arr, y, x + 1), n - 1, history, [le.__name__, y, x + 1])
				funcs = [one,two,three,four]
				shuffle(funcs)
				for f in funcs:
					f()


go(grid)
