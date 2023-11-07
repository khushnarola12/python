#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def greet(name='java'):
    print("hi",name)

greet('python')


# In[ ]:


def wish(name,msg):
    print("hello",name,msg)

wish("java","good morning")


# In[ ]:


def wish(name,msg):
    print("hello",name,msg)

wish("java","good morning")
wish(name="c++","good morning")


# In[ ]:


def sum(*n):
    total=0
    for i in n:
        total+=i
    print("the total is",total)
sum(1,2)
sum(1,4)
sum(1,4,5,3,2)


# In[ ]:


def display(**kwargs):
    for key,value in kwargs.items():
        print(key,":",value)
display(name="python")
display(name="java",age=100)


# In[ ]:


def display(**kwargs):
    for key,value in kwargs.items():
        print(key,":",value)
display(name="python")
display(name="java",age=100)
display(name="khush narola",age=243)


# In[ ]:


def func():
    z=60
    print(z)
func()
print(z)


# In[ ]:


z=100
def func():
    global z
    z=60
    print(z)
func()
print(z)


# In[ ]:


#wap to get integer solution of x^2 - 2y^2=1 for range 1 to 100 def sum(*n):
#     total=0
#     for i in n:
#         total+=i
#     print("the total is",total)
# sum(1,2)
# sum(1,4)
# sum(1,4,5,3,2)
def func():
    for i in range(1,100):
        y = (((i**2)+1)/2)**(1/2)
        z= i**2-2*y**2
        if z==1:
            print(y)
        else:
            print("try again")
        
func()


# In[ ]:


for x in range(1,101):
    for y in range(1,101):
        if x**2-2*y**2==1:
            print(x,y)


# In[13]:


#wap that given an amount of change lessthan 1$ it will print out exactly how many qaurters,dines,nickels,pennys
d = float(input("enter a dollar less than 1 dollar"))
d=d*100
print(d//25,"qaurter")
d=d%25
print(d//10,"dime")
d=d%10
print(d//5,"nickel")
d=d%5
print(d//1,"penny")
d=d%1
        


# In[9]:


#wap suppose you put 1 rupees in bank on first daY(monday) and everyday from next day(tuesday to sunday) you put in one rupee
#more than before and on subsequint monday you put one rupee more than monday if we have total amount of money you will have in
#account in nth day
day=16
week = day//7
sum = 28
total = 2*(sum)+7
day =day%7
total =total + (day+week)+(day-1+week)
print(total)
    


# In[6]:


for i in 6
    for j in 6


# In[ ]:




