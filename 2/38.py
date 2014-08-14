dbg = 0

results = []

def exclude(arr,n):
	if type(n) is list:
		return [j for j in arr if j not in n]
	ret = [j for j in arr if j != n]
	return ret

def trymov(left, right, history, t):
	cnt = len(history)
	
	if dbg:
		print '>'*len(history), history
		raw_input()

	if [left,right] in history:
		return
	history.append([left,right])

	if cnt > 25:
		return

	if len(left) == 0:
		print t,history
		return
	
	if cnt % 2 == 0:
		if len(left) == 1:
			trymov([], right + [left[0]], history, t + left[0])
		else:
			for a in left:
				for b in exclude(left, a):
					trymov(exclude(left,[a,b]), right + [a,b], history, t + max(a,b))
	else:
		for a in right:
			trymov(left + [a], exclude(right, a), history, t + a)

trymov([1,2,4,6], [], [], 0)
