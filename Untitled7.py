#!/usr/bin/env python
# coding: utf-8

# In[2]:


number = int(input("enter num "))
if number%2==0:
    print("number is even")
else:
    print("number is odd")


# In[8]:


#take 3 input from user and give the largest 
num1 = int(input("enter A"))
num2 = int(input("enter B"))
num3 = int(input("enter C"))

if num1>num2:
    if num1>num3:
        print("A is largest")
    else:
        print("C is largest ")
elif num2>num3:   
    print("B is largest")
else:
    print("C is largest")


# In[18]:


#wap to check if number is divisible by 7 and 6
num = int(input("enter number "))
if num%6==0:
    if num%7==0:
        print("number is divisible")
    else:
        print("not divisible")
else:
    print("not divisible")


# In[27]:


num = int(input("enter year "))
if num%4==0:
    if num%100==0:
        if num%400==0:
            print("leap year")
        else:
            print("not leap year")
       
    else:
        print("leap year")
else:
    print("not divisible")


# In[ ]:





# In[ ]:




