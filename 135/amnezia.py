import ipaddress
def log(a):
    if a=='1': return(True)
    else: return(False)
A=[]
c=log(input())

with open('1488.txt') as f:
  a=f.readlines()
for i in a:
  if i not in A:
    print('{')
    print(f'    "hostname": "{i.rstrip()}"')
    print('    "ip": ""')
    print('},')
    A.append(i)