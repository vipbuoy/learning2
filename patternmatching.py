#regex for phone number matching!!!
import re
phonenumber=re.compile(r'(\+?\d*)?(\d{10})')
s=input("Enter string:")
l1=[]
found=phonenumber.findall(s)
for j in found:
    if j[0]=='':
        l1.append(j[1])
    else:
        l1.append('-'.join(j))

for i in l1:
    print(i)


#regex for email address!!!
email=re.compile(r'(\w+)@(\w{2,})\.(\w{2,3})(\.\w{2,3})?')
s=input("Enter string:")
l2=[]
found=email.findall(s)
for j in found:
    t=''
    t=j[0]+'@'+j[1]
    t=t+'.'+j[2]
    if j[3]!='':
        t=t+j[3]
    l2.append(t)

for i in l2:
    print(i
          )
    
