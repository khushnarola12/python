#!/usr/bin/env python
# coding: utf-8

# In[1]:


print('hello')


# In[2]:


x = None
print(type(x))


# In[3]:


x=[1,2,3]
print(type(x))


# In[4]:


x = (1,2,3)
print(type(x))


# In[5]:


x = 'python'
print(type(x))


# In[6]:


x = {1,2,3,3}
print(x)


# In[7]:


x = {1:'python',
    2:'java'}
print(x)
print(type(x))


# In[8]:


a =50
print(id(a))


# In[9]:


a ='khush'
print(id(a))


# In[10]:


a= 50
b=50
print(id(a))
print(id(b))


# In[11]:


a=1000
b=1000
print(id(a))
print(id(b))


# In[12]:


del a


# In[13]:


print(a)


# In[ ]:


print(b)


# In[ ]:


a =50
b =float(a)
print(b)


# In[ ]:


b=str(a)
print(b)


# In[ ]:


3e300*43e400


# In[ ]:





# In[ ]:


'''a = 500
b = 8
speed = a/b
print(speed)'''


# In[ ]:


# comment
dir(__builtins__)


# In[ ]:


Fprint


# In[ ]:


print()


# In[ ]:


print('khush')


# In[ ]:


print(print('helloworld'))


# In[ ]:





# In[ ]:


name='python'
age =35
print("the name is",name,'age is',age)


# In[ ]:


name='python'
age =35
print(f"the name is {name} age is {age}")


# In[ ]:


print('this is')
print('on second line')


# In[ ]:


print('this is',end="")
print(' on second line')


# In[ ]:


print('apple','banana','cherry')


# In[ ]:


print('apple','banana','cherry',sep=".")


# In[ ]:


print('apple','banana','cherry',sep=",")


# In[ ]:


help(print)


# In[ ]:


import this


# In[ ]:


#distance is in kelometers
distance = 500
#time is in hour
time = 8
#speed is in km/hr
speed = distance/time
print('the speed of car is ',speed,'km/hr')


# In[ ]:


#input function.
#it takes prompt from user
#display prompt from user
#user can type or response
#it returns user input as string
input()


# In[ ]:


print('enter a radius')
input("radius")
area = 3.14*radius*radius
parameter = 2*3.14*radius
print('the area of circle',area,'m^2 and','parameter is',parameter,'meter')


# In[ ]:


df


# In[ ]:


print('enter a radius')
a = float(input("radius"))

print(3.14*a*a)


# In[ ]:





# In[ ]:





# In[ ]:


input()


# In[ ]:





# In[ ]:





# In[ ]:


a =input("radius")
r = float(a)
print(3.14*r*r)


# In[ ]:


import math


# In[1]:


# python logical operators
# not x = returns true if x is false,true otherwise
# x and y = returns x if x is false , y otherwise
# x or y = return y if x is false , x otherwise
x=6
not x


# In[2]:


x = 6
not 6


# In[3]:


x = 0
not 0


# In[4]:


x = None
not x


# In[5]:


x=""
not x


# In[6]:


5 and 6


# In[7]:


4 and 4


# In[8]:


10 and 11


# In[9]:


0 and 11


# In[10]:


5 or 6


# In[11]:


0 or 1


# In[12]:


0 and 1


# In[16]:


#MEMBERSHIP OPERATOR
 print('p' in 'python')


# In[ ]:





# In[17]:


"p" in "python"


# In[18]:


#ternary operator
result = "even" if (10%2==0) else"odd"
print(result)


# In[19]:


-2**2


# In[20]:


2**3**2


# In[21]:


0 or 'hello' and 1


# In[22]:


100+200/10 -3*10


# In[ ]:




