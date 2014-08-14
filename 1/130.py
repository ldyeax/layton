from copy import deepcopy

def valid(board):
	def cvalid(ncol):
		for c in [x for x in range(len(board)) if x != ncol]:
			xdist = ncol - c

			attacked_rows = [ board[ncol], board[ncol] + xdist, board[ncol] - xdist ]
			
			if board[c] in attacked_rows:
				return False
		return True

	for ncol in range(len(board)):
		if not cvalid(ncol):
			return False
	
	return True
		

def bs(b):
	return " ".join([str(x) for x in b])

def tryboard(b = [], n = 0):
	board = deepcopy(b)
	board.append(n)
	if valid(board):
		if len(board) == 8:
			print bs(board)
		for i in range(8):
			tryboard(board, i)

for i in range(8):
	tryboard([], i)
