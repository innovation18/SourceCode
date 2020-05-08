#!/usr/bin/env python
# coding: utf-8

# # Generating Rainbow Tables

# ## Set Up

# In[ ]:


# Load the NIST list of 10,000 most commonly used passwords
with open('nist_10000.txt', newline='') as bad_passwords:
    nist_bad = bad_passwords.read().split('\n')
print(nist_bad[1:10])


# In[2]:


# The following data is a normalized simplified user table
# Imagine this information was stolen or leaked
leaked_users_table = {
    'jamie': {
        'username': 'jamie',
        'role': 'subscriber',
        'md5': '203ad5ffa1d7c650ad681fdff3965cd2'
    }, 
    'amanda': {
        'username': 'amanda',
        'role': 'administrator',
        'md5': '315eb115d98fcbad39ffc5edebd669c9'
    }, 
    'chiaki': {
        'username': 'chiaki',
        'role': 'subscriber',
        'md5': '941c76b34f8687e46af0d94c167d1403'
    }, 
    'viraj': {
        'username': 'viraj',
        'role': 'employee',
        'md5': '319f4d26e3c536b5dd871bb2c52e3178'
    },
}


# In[ ]:


# import the hashlib
import hashlib 
# example hash
word = 'blueberry'
hashlib.md5(word.encode()).hexdigest()


# ## Your Task!
# ### Use the information above and hashlib to:
# 1. Create a python dictionary for each word in the `nist_bad` list. For each word, the dictionary should use the hashlib.md5 string as a key, and the word as the value.
# 
# 2. Iterate over each user in the `leaked_users_table` dictionary and attempt to use the rainbow table to crack their password.

# In[27]:


rainbow_table={}
for word in nist_bad:
    hashed_word = hashlib.md5(word.encode()).hexdigest()
    rainbow_table[hashed_word] = word
        
for user in leaked_users_table.keys():
    try:
        print(user + ":\t" + rainbow_table[leaked_users_table[user]['md5']])
    except:
        print('not found')
        


# <span class="graffiti-highlight graffiti-id_uypmj06-id_r7srxv6"><i></i><button>I'm Stuck! Show Solution</button></span>
