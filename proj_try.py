import matplotlib.pyplot as mp
import random

def partition(l1,start,end,l2):
    i=start+1
    pivot=l1[start]
    j=end
    #print(start,end)
    plot(l2,l1,0,0,start,True)
    while i <= j:
        if l1[i]<pivot:
            i+=1
        if l1[j]>=pivot:
            j-=1
        if i<=j and l1[i]>pivot and l1[j]<pivot:
            #l1[i],l1[j]=l1[j],l1[i]
            #print(l1[i],l1[j],pivot)
            temp=l1[i]
            l1[i]=l1[j]
            l1[j]=temp
            #i+=1
            #j-=1
            #print("swapped")
        #print(l1,i,j)
        plot(l2,l1,i,j,start,True)
    #l1[start],l1[j]=l1[j],l1[start]
    temp=l1[start]
    l1[start]=l1[j]
    l1[j]=temp
    #print(l1,j)
    return j
        
def quick(l1,start,end):
    #print(l1)
    l2=list(range(len(l1)))
    if start<end:
        p=partition(l1,start,end,l2)
        #print(p)d
        #d1=dict()
        #count=0
        #for i in l1:
        #    d1[count]=i
        #    count+=1
        #plot(d1)
        quick(l1,start,p-1)
        quick(l1,p+1,end)
        #print(l2)
        #plot(l1,l2)
def plot(l2,l1,i,j,pivot,flag):
    #mp.pyplot(list(d1.keys()),list(d1.values(),color="BLACK"))
    temp=mp.bar(l2,l1)
    mp.title("Quick Sort")
    if flag :
        if i<len(l2) and j<len(l2):
            #print(i,j)
            temp[i].set_color('r')
            temp[j].set_color('r')
            temp[pivot].set_color('g')
            mp.title("Quick Sort")
            mp.show(block=False)
            mp.pause(0.2)
            mp.clf()
        else:
            mp.show(block=False)
            mp.pause(0.2)
            mp.clf()
    else:
        
        mp.show()
#l1=[1,4,5,2,3,7,41]
l1=list()
n=20
#for i in range(20):
    #    l1.append(random.ra)%100)
#    l1.append(random.randrange(100))
#l1=[76, 35, 60, 88, 60, 32, 67, 75, 73, 66, 77, 93, 33, 0, 57, 74, 75, 7, 10, 77]
i=0
d1=dict()
while i<n:
    temp=random.randrange(n)
    if temp in d1:
        continue
    else:
        d1[temp]=0
        l1.append(temp)
        i+=1
print(l1)
quick(l1,0,len(l1)-1)
l2=list(range(20))
print(l1)
plot(l2,l1,0,0,0,False)

#print(l1)
#l2=[10,80,30,90,40,50,70]
#quick(l2,0,len(l2)-1)
#print(l2)
#[76, 35, 60, 88, 60, 32, 67, 75, 73, 66, 77, 93, 33, 0, 57, 74, 75, 7, 10, 77]
