import random

def txtrandint(filename,listSize,minRange,maxRange):
    #Creates a .txt file containing a string of random integers.
    #Outputs a list containing those random integers.
    L=[]
    F = open(filename, 'w+')
    for i in range(0,listSize):
        r = random.randrange(minRange,maxRange)
        L.append(r)
        F.write('%s ' % r)
    return L

