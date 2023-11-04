#!/usr/bin/env python
# coding: utf-8

# In[ ]:


i=0
while i<5:
   print(i)
   i+=1


# In[ ]:


#wap take 3 user input a,b,c and check how many numbers between a and b are divisible by C
a= int(input("enter a"))
b=int(input("enter b"))
c=int(input("enter c"))
count=0
for i in range(a+1,b):
    if(i%c==0):
        count+=1
        print(i)

print(count)


# In[ ]:


a = int(input("enter a number of febonacci"))
d=0;
b=0;
c=1;
while d<a:
    print(b)
    b=c
    c=a+b
    d+=1
   


# In[ ]:


a = int(input("enter a number of febonacci   "))
d=0;
b=0;
c=1;
while d<a:
    print(b)
    e=b+c
    b=c
    c=e
   
    d+=1
   


# In[ ]:


#wap armstrong
num = int(input("enter a number"))
a=num
b=num
count=0;
sum=0
while a>0:
    count+=1
    a=a//10

while b>0:
    c=b%10
    sum = sum + c**count
    b=b//10

if num==sum:
    print("Armstrong")
else:
    print("Not Armstrong")


# In[ ]:


2**3


# In[ ]:


#wap armstrong
num = int(input("enter a number "))
a=num
b=num
count=0;
sum=0
while a>0:
    count+=1
    a=a//10

while b>0:
    c=b%10
    sum = sum + c**count
    b=b//10

if num==sum:
    print("Armstrong")
else:
    print("Not Armstrong")


# In[20]:


x=4
for i in range (x):
    for j in range (i):
        print("*",end="")
    print("")
    


# In[ ]:


#function take an inpu


# In[11]:


def add(x,y):
    """ 
    this function adds 2 numbes x&y
    parameters:
    x=int
    y=int
    output x+y
    """
    return x+y

add()


# In[8]:


help(range)


# In[15]:


x=90
def display():
    global x
    x=60
    print(x)
display()
print(x)


# In[27]:


def calc(x,y):
    sum = x+y
    sub = x-y
    div = x/y
    mul = x*y
    flowdiv = x//y
    mod = x%y
    
    return sum,sub,div,mul,flowdiv,mod
   

x=calc(3,32)
print(type(x))
print(x)


# In[3]:


#default argument

def wish(name="guest"):
    print("hello",name)
wish("john")


# In[ ]:




