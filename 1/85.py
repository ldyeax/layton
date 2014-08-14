def d(t):
	b1 = 180
	g1 = t - b1
	g2 = 150
	b2 = t - g2
	print b1, g1, b2, g2, t
	return abs((b1 + b2) - (g1 + g2))

for i in range(10):
	print d(200 + i * 10)
