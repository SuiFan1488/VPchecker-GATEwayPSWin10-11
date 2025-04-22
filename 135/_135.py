import ipaddress
def log(a):
    if a!='0': return(a)
    else: return(False)
A=[]
NAME="_135"
def callzeroargs(interface):
    with open('1488.txt') as f:
      a=f.readlines()
    for i in a:
      if i not in A:
        print(f'route -p add {i.rstrip()} "{interface}"')
        A.append(i)
def call(b,interface):
    with open(f'{b}') as f:
      a=f.readlines()
    for i in a:
      if i not in A:
        print(f'route -p add {i.rstrip()} "{interface}"')
        A.append(i)
def deletecall(b):
    with open(f'{b}') as f:
      a=f.readlines()
    for i in a:
        if i not in A:
            print(f'route delete {i.rstrip()}')
            A.append(i)