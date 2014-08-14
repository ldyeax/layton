from copy import deepcopy

s = "             \n xxxxx xxxxx \n xxxxx xxxxx \n             \n xx xxxxx xx \n xx xxxxx xx \n xx       xx \n xx xxxxx xx \n xx xxxxx xx \n             \n xxxxx xxxxx \n xxxxx xxxxx \n             "

orig = [[c for c in ss] for ss in s.split("\n")]

solution = [[]]

def fitness(arr):
	return sum([row.count('p') for row in arr])

dbg = 0

def print_map(arr):
	print " " + "="*13
	for row in arr:
		print "|" + "".join(row) + "|"
	print " " + "="*13

def recurse(a, y, x):
	if y < 0 or y >= len(a) or x < 0 or x >= len(a[0]):
		return
	
	arr = deepcopy(a)

	if arr[y][x] != ' ':
		return
	arr[y][x] = 'p'
	
	if dbg:
		print_map(arr)
		raw_input()

	if y == len(arr) - 1 and x == 0:
		if fitness(arr) > fitness(solution[0]):
			solution[0]=arr
			print "solution!"
		return
	
	recurse(arr, y + 1, x)
	recurse(arr, y - 1, x)
	recurse(arr, y, x + 1)
	recurse(arr, y, x - 1)

recurse(orig, 0, 12)

print_map(solution[0])
