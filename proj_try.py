import matplotlib.pyplot as mp


def partition(l1,start,end):
    i=start+1
    pivot=l1[start]
    j=end
    #print(start,end)
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
    #l1[start],l1[j]=l1[j],l1[start]
    temp=l1[start]
    l1[start]=l1[j]
    l1[j]=temp
    #print(l1,j)
    return j
        
def quick(l1,start,end):
    if start<end:
        p=partition(l1,start,end)
        #print(p)d
        #d1=dict()
        #count=0
        #for i in l1:
        #    d1[count]=i
        #    count+=1
        #plot(d1)
        l2=[range(len(l1))]
        plot(l2,l1)
        quick(l1,start,p-1)
        quick(l1,p+1,end)
def plot(l2,l1):
    #mp.pyplot(list(d1.keys()),list(d1.values(),color="BLACK"))
    mp.plot(l2,l1)
    mp.show()
l1=[1,4,5,2,3,7,41]
quick(l1,0,len(l1)-1)
print(l1)
l2=[10,80,30,90,40,50,70]
quick(l2,0,len(l2)-1)
print(l2)
