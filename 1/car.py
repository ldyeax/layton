from copy import deepcopy

grid = [ [51, 0, 0, 0, 2, 2], [51, 3, 3, 0, 0, 0], [0, 0, 54, 0, 0, 55], [6, 6, 54, 57, 0, 55], [58, 9, 9, 57, 0, 60], [58, 11, 11, 12, 12, 60] ]

def can_escape(arr):
	row = arr[3]
	for sq in row:
		if sq not in [0, 6]:
			return False
	return True

def left(a, y, x):
	if x <= 0:
		return None
	arr = deepcopy(a)
	row = arr[y]
	if row[x - 1] != 0:
		return None
	sq = row[x]
	i_x = x
	while True:
		i_x -= 1
		if i_x < 0 or row[i_x] != 0:
			return arr
		row[i_x] = sq
		row[i_x + 2] = 0

def right(a, y, x):
	if x >= 4:
		return None
	arr = deepcopy(a)
	row = arr[y]
	if row[x + 2] != 0:
		return None
	sq = row[x]
	i_x = x
	while True:
		i_x += 1
		if i_x > 5 or row[i_x] != 0:
			return arr
		row[i_x + 1] = sq
		if i_x - 2 > 0:
			row[i_x - 2] = 0

def up(a, y, x):
	if y <= 0:
		return None
	arr = deepcopy(a)
	
	if arr[y - 1][x] != 0:
		return None
	
	sq = arr[y][x]
	i_y = y
	while True:
		i_y -= 1
		if i_y < 0 or arr[i_y][x] != 0:
			return arr
		print(i_y)
		arr[i_y][x] = sq
		arr[i_y + 2][x] = 0

def dn(a, y, x):
	if y >= 4:
		return None
	arr = deepcopy(a)

	if arr[y + 2][x] != 0:
		return None
	
	sq = arr[y][x]
	i_y = y
	while True:
		i_y += 1
		if i_y > 4 or arr[i_y][x] != 0:
			return arr
		arr[i_y][x] = sq
		arr[i_y - 1][x] = 0

def search(arr, n = 14, history = ""):
	if arr == None:
		return
	if n <= 0:
		return
	if can_escape(arr):
		print(len(history))
		print(history)

	prev_lr = None
	prev_ud = None
	for y in range(6):
		for x in range(6):
			sq = arr[y][x]
			if sq > 0:
				if sq < 50 and sq != prev_lr:	
					search(left(arr, y, x), n - 1, history + "left@" +str(y)+","+str(x)+"; ")
					search(right(arr,y, x), n - 1, history + "right@"+str(y)+","+str(x)+"; ")
					prev_lr = sq
				elif sq != prev_ud:
					search(up(arr, y, x), n - 1, history + "up@"+str(y)+","+str(x)+"; ")
					search(dn(arr, y, x), n - 1, history + "dn@"+str(y)+","+str(x)+"; ")
					prev_ud = sq

search(grid)
