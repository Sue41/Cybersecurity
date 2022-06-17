#%%
from operator import mod
import string

#%%
def egcd(a, b):
  if a == 0:
      return (b, 0, 1)
  g, y, x = egcd(b%a,a)
  return (g, x - (b//a) * y, y)

def modinv(a, m):
  return egcd(a, m)[1] % m

#%%

mapping = string.ascii_lowercase + string.digits + "_"
print(mapping)
#%%
with open("message.txt") as f:

    txt = f.readline().split()

    txt = [int(n) for n in txt]

    mod41 = [i%41 for i in txt]

    mod_inverse = [modinv(i, 41) for i in mod41]
    
    final_txt = [mapping[i-1] for i in mod_inverse]
    
    flag = "".join(final_txt)
   
    # All in one list comprehension
    #flag = "".join([mapping[modinv(int(i)%41, 41)-1] for i in txt])
#%%
print(flag)
# Add the flag text on picoCTF{}
#%%