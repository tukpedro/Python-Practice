#!/usr/bin/env python
# coding: utf-8

# In[3]:


import getpass

def criptografar(chave, string):
    cripto_chars = []
    for i in range(len(string)):
        chave_char = chave[i % len(chave)]
        cripto_char = chr(ord(string[i]) + ord(chave_char) % 256)
        cripto_chars.append(cripto_char)
    cripto_string = ''.join(cripto_chars)
    return cripto_string

def descriptografar(chave, string):
    cripto_chars = []
    for i in range(len(string)):
        chave_char = chave[i % len(chave)]
        cripto_char = chr((ord(string[i]) - ord(chave_char) + 256) % 256)
        cripto_chars.append(cripto_char)
    cripto_string = ''.join(cripto_chars)
    return cripto_string


msg = getpass.getpass('Digite a msg: ')
chave = getpass.getpass('Digite a chave: ')
e = criptografar(chave, msg)
d = descriptografar(chave, e)

print('-'*(len(e)+2))
print(f' {e}')
print('-'*(len(e)+2))

desc = str(input('Deseja descriptografar? S/N: ')).lower()
while desc != 's' and desc != 'n':
    desc = str(input('Digite S ou N: ')).lower()
    
if desc == 's':
    c = getpass.getpass('Digite a chave: ')
    while c != chave:
        print('CHAVE INCORRETA')
        c = getpass.getpass('Digite a chave: ')
    print('-'*(len(e)+2))
    print(f' {d}')
    print('-'*(len(e)+2))


# In[ ]:




