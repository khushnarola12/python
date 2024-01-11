#!/usr/bin/env python
# coding: utf-8

# In[ ]:





# In[2]:


f=open("Desktop/worked_exercises_text_files/wordlist.txt")
words = [line.strip() for line in open("Desktop/worked_exercises_text_files/wordlist.txt")]
for word in words:
    if len(word)>=6:
        if word[0:3]==word[-3:]:
            print(word)
        


# In[11]:


f=open("Desktop/worked_exercises_text_files/wordlist.txt")
words = [line.strip() for line in open("Desktop/worked_exercises_text_files/wordlist.txt")]
count=0
words2 = len(words)
for word in words:
    if 'a' in word and 'e'in word and 'i'in word and 'o' in word and 'u' in word:
        count=count+1
        
print(count)
print(words2)
per = count/words2)


# In[ ]:


f=open("Desktop/worked_exercises_text_files/wordlist.txt")
words = [line.strip() for line in open("Desktop/worked_exercises_text_files/wordlist.txt")]
max=0
for word in words:
    if :
        if word[0]==word[-1]:
            if len(word)>max:
                long=word
                max = len(word)                
print(max)
print(long)


# In[ ]:




