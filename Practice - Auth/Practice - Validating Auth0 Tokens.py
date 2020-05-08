#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# Install a pip package in the current Jupyter kernel
import sys
get_ipython().system('{sys.executable} -m pip install python-jose')


# In[ ]:


import json
from jose import jwt
from urllib.request import urlopen


# In[ ]:


# Configuration
# UPDATE THIS TO REFLECT YOUR AUTH0 ACCOUNT
AUTH0_DOMAIN = 'fsnd.auth0.com'
ALGORITHMS = ['RS256']
API_AUDIENCE = 'image'


# In[ ]:


'''
AuthError Exception
A standardized way to communicate auth failure modes
'''
class AuthError(Exception):
    def __init__(self, error, status_code):
        self.error = error
        self.status_code = status_code


# In[ ]:


# PASTE YOUR OWN TOKEN HERE
# MAKE SURE THIS IS A VALID AUTH0 TOKEN FROM THE LOGIN FLOW
token = "eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsImtpZCI6Ik56Z3lSVFZEUmpKQ1FrUkJSRGN3TjBReFJUQTFPVUl5UlRORk9EQXhPVGMwTmpjNU9USkVPQSJ9.eyJpc3MiOiJodHRwczovL2ZzbmQuYXV0aDAuY29tLyIsInN1YiI6ImF1dGgwfDVkMDNkM2U2NzI2YjhmMGNiNGJmNzFjOSIsImF1ZCI6ImltYWdlIiwiaWF0IjoxNTYwNTU2MTc0LCJleHAiOjE1NjA1NjMzNzQsImF6cCI6ImtpNEI2alprdUpkODdicEIyTXc4emRrajFsM29mcHpqIiwic2NvcGUiOiIiLCJwZXJtaXNzaW9ucyI6WyJnZXQ6aW1hZ2VzIiwicG9zdDppbWFnZXMiXX0.ENxNT1lo_sX9rpgmGJmiu14lugmYXqb8siJwC1nPuGSb_ycK02KyS5IkA-YkhySMBcDD5IJfawPkJNmJPtUAB1wYVP8hlNsBuvLjtYxzH_VHNeXzVXWQvM7RiuPwrmWJmJN2onmZPh3bjiUZxvyAp0Yp0Rvm54SsiDjO_Dj1Qx-Az_Zjo-mY2ECfFgAo0ifnqDMIgE5YDZ3uOzMni4oEU5Ok-TrQOSwyfJyUC1KQ7ubQ-Bnbh-0Aii9UK9R4JBH7iIMva8_edQkgR4MuRXatYhsqvHsxQ2Iv5rjMmTAmjknsYWE5VYrzafRGVigbPD9A6ELEnyjADBQ9vMtSdPQe2w"


# In[ ]:


## Auth Header
def verify_decode_jwt(token):
    # GET THE PUBLIC KEY FROM AUTH0
    jsonurl = urlopen(f'https://{AUTH0_DOMAIN}/.well-known/jwks.json')
    jwks = json.loads(jsonurl.read())
    
    # GET THE DATA IN THE HEADER
    unverified_header = jwt.get_unverified_header(token)
    
    # CHOOSE OUR KEY
    rsa_key = {}
    if 'kid' not in unverified_header:
        raise AuthError({
            'code': 'invalid_header',
            'description': 'Authorization malformed.'
        }, 401)

    for key in jwks['keys']:
        if key['kid'] == unverified_header['kid']:
            rsa_key = {
                'kty': key['kty'],
                'kid': key['kid'],
                'use': key['use'],
                'n': key['n'],
                'e': key['e']
            }
    
    # Finally, verify!!!
    if rsa_key:
        try:
            # USE THE KEY TO VALIDATE THE JWT
            payload = jwt.decode(
                token,
                rsa_key,
                algorithms=ALGORITHMS,
                audience=API_AUDIENCE,
                issuer='https://' + AUTH0_DOMAIN + '/'
            )

            return payload

        except jwt.ExpiredSignatureError:
            raise AuthError({
                'code': 'token_expired',
                'description': 'Token expired.'
            }, 401)

        except jwt.JWTClaimsError:
            raise AuthError({
                'code': 'invalid_claims',
                'description': 'Incorrect claims. Please, check the audience and issuer.'
            }, 401)
        except Exception:
            raise AuthError({
                'code': 'invalid_header',
                'description': 'Unable to parse authentication token.'
            }, 400)
    raise AuthError({
                'code': 'invalid_header',
                'description': 'Unable to find the appropriate key.'
            }, 400)

