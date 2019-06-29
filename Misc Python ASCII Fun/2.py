import time
import os

delay = 0.05 #seconds 
long_delay = 10
X = 10
Y = 10
BEFORE = "O" 
AFTER = "X"

clear = lambda: os.system('cls') #clears screen 

rows = []
for a in range(0,Y):
	column = []
	for b in range(0,X):
		column.append(BEFORE)
	rows.append(column)

right_a = 0
down_a, down_b = 0, len(rows[0]) - 1
left_a, left_b = len(rows[0]) - 1, len(rows[0]) - 1
up_a, up_b = len(rows[0]), 0

def print_all():
	global iterations

	for a in range(len(rows)):
		print(''.join(rows[a]))
		
	iterations += 1
	time.sleep(delay)
	clear()


iterations = 0

while True:
	#right
	if iterations == X * Y:
		break
	for a in range(len(rows[right_a])):
		if rows[right_a][a] == BEFORE:
			rows[right_a][a] = AFTER
			print_all()
	right_a += 1

	#down
	if iterations == X * Y:
		break
	for a in range(len(rows[right_a])):
		if rows[a][down_b] == BEFORE:
			rows[a][down_b] = AFTER
			print_all()
	down_b -= 1

	#left
	if iterations == X * Y:
		break
	for a in range(len(rows[right_a])):
		reverse = (len(rows[right_a]) - a) - 1
		if rows[left_a][reverse] == BEFORE:
			rows[left_a][reverse] = AFTER
			print_all()
	left_a -= 1

	#up
	if iterations == X * Y:
		break
	for a in range(len(rows[right_a])):
		reverse = (len(rows[right_a]) - a) - 1
		if rows[reverse][up_b] == BEFORE:
			rows[reverse][up_b] = AFTER
			print_all()
	up_b += 1
	
while True: 
	clear()
	print_all()
	time.sleep(long_delay)
	


