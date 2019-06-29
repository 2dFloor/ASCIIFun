import time
import os

delay = 0.1 #seconds 
original_line = []
size = 20

clear = lambda: os.system('cls') #clears screen 

while True:
	del original_line[:]
	for a in range(size):
		original_line.append("*")
	"".join(original_line)

	for x in range(size):
		for z in range(size):
			copy = list(original_line)
			pos = z + x

			if pos > size - 1:
				pos = pos - size
			
			copy[pos] = " "
			print("".join(copy))
				
	
		time.sleep(delay)
		clear()	
	

	