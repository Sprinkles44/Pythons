import oscarlib

Input = oscarlib.txtrandint('blah.txt',34,-100,100)

ncount = 0  # Number of negatives
pcount = 0  # Number of positives
nsum = 0  # Sum of negatives
psum = 0  # Sum of positives

for val in Input:
    if val < 0:
        nsum = nsum+val
        ncount = pcount+1
    elif val > 0:
        psum = psum+val
        pcount = pcount+1

# Calculating the averages
navg = round(nsum/ncount,3)
pavg = round(psum/pcount,3)

# Printing the averages
print("\n")
print("Avg of negative numbers:\t\t" + repr(navg) + "\n")
print("Avg of non-negative numbers:\t" + repr(pavg) + "\n")
