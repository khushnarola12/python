#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#STRIP METHOD REMOVES LEADING AND TRAILING CHARATERS FROM GIVEN STRING
help(str.strip)


# In[ ]:


s="khush"
help(s.strip)


# In[ ]:


x="h      khush      h"
x.strip('h')


# In[ ]:


help(s.maketrans())
help(s.translate())


# In[ ]:





# In[ ]:


intab="aitou"
outtab ="12345"
my="this is my string function"
table=my.maketrans(intab,outtab)
print(my.translate(table))
print(table)


# In[ ]:


import string
a_string="hi !s fsdfds@#43r5dk dkjssdkj[] fsd#$t4"
new_string = a_string.translate(str.maketrans('s','l',string.punctuation))
print(new_string)


# In[ ]:


#tuple is d.s. which is immutable and can be a mixture of multiple datatypes it can be created using coma and parenthesis .
x=()
type(x)


# In[ ]:


x=(6,)
type(x)


# In[ ]:


x=1,2,4
type(x)
print(x)


# In[ ]:


x=(1,2,'hi',[1,2,3])
x[3][2]=100
print(x)


# In[ ]:


x=(1,2,3,4,5,6)
print(x[0:5:1])


# In[ ]:


help(sorted)


# In[ ]:


x=('hii','hi','python','GSSDGDSFSADSF')
sorted(x,reverse=True)
sorted(x,key=len,reverse=True)


# In[ ]:


help(tuple)


# In[ ]:


x=("hii","gsd","fdfsggf")
print(x.count('g'))
print(x.index('i'))


# In[ ]:


#wap if string is palindrom 
s = input("Enter a string")
b = s[::-1]
if s==b:
    print("palindrom")
else:
    print("not palindrom")


# In[1]:


#count no of uppercase and lowercase in string
s = input("Enter a string   -")
countu=0
countl=0


for i in s:
    if i.isupper():
        countu+=1
    else:
        countl+=1
        
print("upper c",countu)
print("lower c",countl)


# In[7]:


s = input("Enter a string  ")
b=len(s)
print(s[0])
print(s[b-1])
print(s[b//2])


# In[19]:


#calculate the sum and average of digit in string
s= input("Enter a string")
sum=0
b=len(s)
count=0
for i in s:
    if i.isdigit():
    
        sum=sum+int(i)
    else:
        count=count+1
 


print(sum)   
avg = (sum/(b-count))
print(avg)


# In[ ]:




