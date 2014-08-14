fertile = 1
young1 = 0
young2 = 0

month = 1
while month <= 10:
	if month % 2:
		fertile += young1
		young1 = fertile * 12
	else:
		fertile += young2
		young2 = fertile * 12
	
	print fertile, young1, young2

	month += 1

print fertile + young1 + young2
