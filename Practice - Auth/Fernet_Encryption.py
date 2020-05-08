#!/usr/bin/env python
# coding: utf-8

# > TIP: Remember, code with dotted lines has a tool tip and voice walkthrough!

# In[ ]:


# Import Package
from cryptography.fernet import Fernet


# In[ ]:


# Generate a Key and Instantiate a Fernet Instance
key = Fernet.generate_key()
f = Fernet(key)
print(key)


# In[ ]:


# Define our message
plaintext = b"encryption is very useful"


# In[ ]:


# Encrypt
ciphertext = f.encrypt(plaintext)
print(ciphertext)


# In[ ]:


# Decrypt
decryptedtext = f.decrypt(ciphertext)
print(decryptedtext)

