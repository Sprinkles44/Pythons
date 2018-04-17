import numpy as np
import random as rand
import math

# **********************************************************************************************************************
n = 50  # Number of planes
with open('planeList.txt','w+') as file:
	for i in range(0,n):
		string = chr(rand.randint(65,90)) + str(rand.randint(100,999)) + "," + str(rand.randint(0,1500)) + "," + str(rand.randint(0,1500)) + "," + str(rand.randint(0,10000)) + "\n"
		file.write(string)
# **********************************************************************************************************************

p_pos = []  # Planes and their current position
with open('planelist.txt','r') as file:
	for line in file:
		p_pos.append(line.split(","))

caut_dist = 750  # Caution Zone distance
caut_p = []  # Planes in the Caution Zone
for i in range(len(p_pos)):
	p1 = p_pos[i]
	x1 = int(p1[1])
	y1 = int(p1[2])
	z1 = int(p1[3])
	for k in np.arange(i+1,len(p_pos)):
		p2 = p_pos[k]
		x2 = int(p2[1])
		y2 = int(p2[2])
		z2 = int(p2[3])
		dist = math.sqrt((x2-x1)**2 + (y2-y1)**2 + (z2-z1)**2)
		if dist < caut_dist:
			if p1[0] not in caut_p:
				caut_p.append(p1[0])
			if p2[0] not in caut_p:
				caut_p.append(p2[0])

for plane in caut_p:
	print(str(plane) + ": You are in the Caution Zone, you must move immediately.\n")
