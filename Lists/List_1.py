#!/usr/bin/env python
# coding: utf-8

# In[2]:


[1,2,3]


# In[3]:


spam = ['cat', 'bat', 'rat', 'pig']
spam


# In[4]:


spam[0]


# In[5]:


'Hello ' + spam[2]


# In[9]:


'the ' + spam[2] + ' ate the ' + spam[-1]


# Getting Sublists with Slices

# In[16]:


spam[:2]


# In[17]:


spam[1:3]


# In[18]:


spam[1:]


# Getting a List's length with len()

# In[20]:


spam = ['cat', 'dog', 'mosse']


# In[21]:


len(spam)


# Changing Values in a list with Indexes

# In[22]:


spam = ['cat', 'bat', 'rat', 'elephant']


# In[23]:


spam[1] = 'ardvark'


# In[24]:


spam


# In[25]:


spam[2] = spam[1]


# In[26]:


spam


# In[27]:


spam[-1] = 12345


# In[28]:


spam


# In[29]:


spam[2] = 'rat'


# In[30]:


spam


# Removing Values from list with del statement

# In[31]:


spam = ['cat', 'bat', 'rat', 'elephant']


# In[32]:


del spam[2]


# In[33]:


spam


# Working with lists

# In[36]:





# Using for Loops with Lists

# In[37]:


for i in range(4):
    print(i)


# In[38]:


for i in [0,1,2,3]:
    print(i)


# In[39]:


supplies = ['pens', 'staples', 'flame-thower', 'binders']


# In[40]:


for i in range(len(supplies)):
    print('Index ' + str(i) + ' in supplies is: ' + supplies[i])


# The In and Not In Operators

# In[ ]:


'howdy' in ['Hello', 'Hi', 'howdy', 'hey']


# In[7]:


myPets = ['Zoe', 'Pooka', 'Jake']
print('Enter a pet name: ')
name = input()

if name not in myPets:
    print('I dont have a pet named ' + name)
else:
    print(name + ' is one of my pets!')


# The Mulitple Assignment Trick

# In[10]:


cat = ['fat', 'black', 'loud']
size, color, disposition = cat


# In[11]:


cat


# In[12]:


size


# In[13]:


color


# In[14]:


disposition


# In[15]:


cat.index('fat')


# In[16]:


size.index


# In[17]:


cat.sort()


# In[18]:


cat


# In[20]:


cat.sort(reverse=True)


# In[21]:


cat


# In[25]:


cat.sort(key=str.upper)
print(cat)


# In[35]:


import random

messages = ['Its is certain', 
           'It is decidedly so',
           'Yes For sure',
           'Reply with haze',
           'ask again later',
           'Please concentrate',
           'My reply is no',
           'Outlook isnt great',
           'Hell Nawl']

print(messages[random.randint(0, len(messages) -1)])


# In[ ]:




