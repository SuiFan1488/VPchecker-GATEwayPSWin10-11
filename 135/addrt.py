import ipaddress
import netresq
from tqdm import tqdm
def main(m):
    with open('a.txt') as f: a=f.readlines()
    with open('1488.txt') as x: b=x.readlines()
    c,F=0,open('14.txt','w')
    for i in tqdm (a, desc="Netresq Wait..."):
        subnet,m = [ipaddress.ip_network(k.rstrip()) for k in b],i.split()[1]
        if m=='(no' or m=='1': m=netresq.dnsresq(i.split()[0])
        if i.split()[1].count('-')>0: m=netresq.dnsresq(i.split()[1]+'.1e100.net')
        elif i.split()[1].count('.')<3: continue
        for subnet1 in subnet:
            if ipaddress.IPv4Address(m) in subnet1: c+=1
        if c!=0: c=0
        else: F.write(f"{netresq.netresq(m)}\n")
        pass
    F.close()
    if m: netresq.countrycheck()
def noterm(m):
    with open('a.txt') as f: a=f.readlines()
    with open('1488.txt') as x: b=x.readlines()
    c,F=0,open('14.txt','w')
    for i in tqdm (a, desc="Netresq Wait..."):
        subnet,m = [ipaddress.ip_network(k.rstrip()) for k in b],i.split()[1]
        if m=='(no' or m=='1': m=netresq.dnsresq(i.split()[0])
        if i.split()[1].count('-')>0: m=netresq.dnsresq(i.split()[1]+'.1e100.net')
        elif i.split()[1].count('.')<3: continue
        for subnet1 in subnet:
            if ipaddress.IPv4Address(m) in subnet1: c+=1
        if c!=0: c=0
        else: F.write(f"{netresq.netresq(m)}\n")
        pass
    F.close()
    if m: netresq.countrycheck()
def nocheck(n):
    with open('a.txt') as f: a=f.readlines()
    c,F=0,open('14.txt','w')
    for i in tqdm (a, desc="Netresq Wait..."):
        m = i.split()[1]
        if m=='(no' or m=='1': m=netresq.dnsresq(i.split()[0])
        if i.split()[1].count('-')>0: m=netresq.dnsresq(i.split()[1]+'.1e100.net')
        elif i.split()[1].count('.')<3: continue
        F.write(f"{netresq.netresq(m)}\n")
        pass
    F.close()
    if m: netresq.countrycheck()
def isinlist(a):
    with open('1488.txt') as d:
        F=d.readlines()
    F,ciunt,N=[ipaddress.ip_network(k.split()[2].rstrip()) for k in F],0,[]
    b=input('from:')
    with open('a.txt') as f:
        A=f.readlines()
    A=[ipaddress.ip_network(k.rstrip()) for k in A]
    for x in F:
        for y in A:
            if y in x: 
                ciunt+=1
                break
    else: N.append(y)
    if ciunt==len(A): print('all in list')
    else: print(N)
