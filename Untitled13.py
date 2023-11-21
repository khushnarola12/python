#!/usr/bin/env python
# coding: utf-8

# In[19]:


def func(a):
    c=a
    sum =0
    while a>0:
        b=a%10
        sum = sum+b
        a=a//10
    if c%sum==0:
        print(c)

num=1
while num<201:
    func(num)
    num=num+1
    


# In[7]:


#wap that promt user to enter numbers and stop only when the user enter quit after 
# this print sum,average,max,min of given numbers enter by the use
sum=0
count=0
max=None
min=None
a=0
while a!="QUIT":
    a = input("enter number")
    if a=="QUIT":
        break
    else:
        b=int(a)
        print(b)
        count=count+1
        sum = sum +b
        if max==None or b>max:
            max=b
        
        if min==None or b<min:
            min=b
   
 
avg=sum/count   
print(avg)
print(sum)
print(max)
print(min)


# #### 
