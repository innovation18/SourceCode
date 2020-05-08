#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Import the Python Library
import sys
get_ipython().system('{sys.executable} -m pip install bcrypt')
import bcrypt


# In[2]:


password = b"securepassword"


# In[3]:


# Hash a password for the first time, with a certain number of rounds
salt = bcrypt.gensalt(14)
password = b"securepassword"

hashed = bcrypt.hashpw(password, salt)
print(salt)
print(hashed)


# In[11]:


# Check a plain text string against the salted, hashed digest
hashed = b'$2b$14$EFOxm3q8UWH8ZzK1h.WTZeRcPyr8/X0vRfuL3/e9z7AKIMnocurBG'
password = b'learningisfun'
bcrypt.checkpw(password, hashed)


# In[ ]:





# In[ ]:




