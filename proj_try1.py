import matplotlib.pyplot as mp
import random

def plot(l1,l2):
    mp.plot(l1,l2)
    mp.show()
def insertion(l1,l2,n):
    for i in range(1, n): 
        plot(l1,l2)
        key = l1[i] 
        # Move elements of arr[0..i-1], that are 
        # greater than key, to one position ahead 
        # of their current position 
        j = i-1
        while j >=0 and key < l1[j] : 
            l1[j+1] = l1[j] 
            j -= 1
        l1[j+1] = key
        

l1=list()
n=100
for i in range(n):
    l1.append(random.randrange(n))

l2=list(range(n))

insertion(l1,l2,n)
plot(l1,l2)
