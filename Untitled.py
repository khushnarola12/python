#!/usr/bin/env python
# coding: utf-8

# In[2]:


i=2
j=4
print(i+j)
i = 'computer'
j = 'lab'
print(i+j)


# In[4]:





# In[7]:


class Pythonprog:
    def __init__(self,fullname):
        self.fullname = fullname
    def show(self):
        print("create of python os "+ self.fullname)

class javaprac:
    def __init__(self,fullname):
        self.fullname = fullname
    def show(self):
        print("crete of java is "+self.fullname)
        
pypr = Pythonprog("roosum")
pypr.show()

javapr = javaprac("james")
javapr.show()


# In[12]:


#inhertitance means aquiring the property to another class the property of a
class person:
    def __init__(self,fullname):
        self.fullname = fullname
    def show(self):
        print(self.fullname +"a python teache")

class professor(person):
    pass

pro = professor("rosss")
per = person("james")
pro.show()
per.show()


# In[13]:


# multilevel inheritance
class person:
    def __init__(self,fullname):
        self.fullname = fullname
    def show(self):
        print(self.fullname +"a python teache")

class professor(person):
    pass
        
class human(professor):
    pass

pro = professor("rosss")
per = person("james")
pre = human("khush")
pro.show()
per.show()
pre.show()


# In[14]:


#hiirarical
class person:
    def __init__(self,fullname):
        self.fullname = fullname
    def show(self):
        print(self.fullname +"a python teache")

class professor(person):
    pass
        
class human(person):
    pass

pro = professor("rosss")
per = person("james")
pre = human("khush")
pro.show()
per.show()
pre.show()


# In[ ]:


class person:
    def __init__(self,fullname):
        self.fullname = fullname
    def show(self):
        print(self.fullname + "is a perspn")
        
class teacher:
    def  credit(self):
        print("he teaches a python")
        
class programmer(person,teacher):
   pass


prog = programmer("James")
prog.show()
prog.credit()
    

