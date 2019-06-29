import time
import os

delay = .5 #seconds 
BACK = "X"
FORE = "O"
clear = lambda: os.system('cls') #clears screen 
WIDTH = 10
HEIGHT = 4

#create all possible frames 
container = []
for i in range(WIDTH):
	original = [None] * WIDTH
	for a in range(WIDTH):
		original[a] = BACK
	original[i] = FORE
	original[(len(original) - i)-1] = FORE		
	container.append(original)

#possibly middle if even number 
if WIDTH % 2 == 0:
	middle = WIDTH / 2
	del container[int(middle)]
#remove last element
del container[-1]


#print("MAIN" + str(container))
trail_tracker = 0
while True:
	for a in range(len(container)):
		print(''.join(container[a]))#top most row, independent of trailing rows
		for b in range(HEIGHT):#trailing rows 
			if a < 2: 
				print(''.join(container[0]))
			else:
				if b < a:
					print(''.join(container[a - b - 1]))
				else:
					print(''.join(container[0]))
		time.sleep(delay)
		clear()	

	
	

	