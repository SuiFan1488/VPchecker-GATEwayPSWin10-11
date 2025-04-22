import ipaddress
from tqdm import tqdm
import netresq
with open('a.txt') as f: a=f.readlines()
with open('1488.txt') as x: b=x.readlines()
for i in tqdm (a, desc="Netresq Wait..."):
    subnet,m = [ipaddress.ip_network(k.rstrip()) for k in b],i.split()[1]
    if m=='(no' or m=='1': m=netresq.dnsresq(i.split()[0])
    if i.split()[1].count('-')>0: m=netresq.dnsresq(i.split()[1]+'.1e100.net')
    elif i.split()[1].count('.')<3: continue
    for subnet1 in subnet:
        if ipaddress.IPv4Address(m) in subnet1: print('TRUE '+m)
    pass