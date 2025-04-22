import ipaddress
with open('a.txt') as f:
    a=f.readlines()
with open('1488.txt') as d:
    b=d.readlines()
c,C,c0=0,[],0
for i in a:
    for k in b:
        subnet1 = ipaddress.ip_network(k.rstrip())
        if i.split()[1]=='(no address)': 
            c0+=1
        if ipaddress.IPv4Address(i.split()[1]) in subnet1:
            c+=1
            C.append(subnet1)
    if c!=0:
        print(i,'true')
        c=0
    else:
        print(i,'false')
print(c0)