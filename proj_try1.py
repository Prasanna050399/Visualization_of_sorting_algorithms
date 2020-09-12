import matplotlib.pyplot as mp
import time
import random

def plot(l1,l2,flag1,flag2,index1,index2,name):
    temp=mp.bar(l1,l2)
    #mp.close()
    mp.title(name)
    if flag1==0 and not flag2:
        mp.show(block=False)
        #time.sleep(2)
        temp[index1].set_color('r')
        temp[index2].set_color('r')
        mp.pause(1)
        #mp.close()
        mp.clf()
    else:
        mp.show()
        
def insertion(l1,l2,n):
    name='Insertion sort'
    for i in range(1, n):
        j=0
        plot(l2,l1,0,False,i,i,name)
        key = l1[i] 
        j = i-1
        while j >=0 and key < l1[j] : 
            l1[j+1] = l1[j] 
            j -= 1
        l1[j+1] = key
        plot(l2,l1,0,False,i,i,name)
        
def selection(l1,l2,n):
    name='selection sort'
    for i in range(n):
        min_ind=i
        for j in range(i+1,n):
            if l1[min_ind]>l1[j]:
                min_ind=j
        plot(l2,l1,0,False,i,min_ind,name)
        l1[i],l1[min_ind]=l1[min_ind],l1[i]
        plot(l2,l1,0,False,i,min_ind,name)




def main():
    l1=list()
    n=20
    d1=dict()
    i=0
    while i<n:
        temp=random.randrange(n)
        if temp in d1:
            continue
        else:
            d1[temp]=0
            l1.append(temp)
            i+=1
    l2=list(range(n))
    #l2.append(9)
    #n+=1
    #l1.append(10)
    print(l1)
    #insertion(l1,l2,n)
    #selection(l1,l2,n)
    def select():
        print("in selection")
        #plot(l1,l2,0,False,0,0,"selection sort")
        selection(l1,l2,n)
        plot(l1,l2,1,True,0,0,'selection sort')
    def insert():
        #plot(l1,l2,0,False,0,0,'Insertion sort')
        insertion(l1,l2,n)
        plot(l1,l2,1,True,0,0,'Insertion sort')
        
    d1=dict()
    d1[1]=select
    d1[2]=insert
    #print(d1[1])
    #temp=d1[1]
    #print(type(temp))
    print("Enter 1 for selection sort\nEnter 2 for insertion sort")
    ans=int(input())
    
    #d1.get(ans,None)
    if ans==1:
        select()
    elif ans==2:
        insert()

if __name__ == "__main__":
    main()
