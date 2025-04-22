import urllib.request
from bs4 import BeautifulSoup
from ipaddress import *
from tqdm import tqdm
NAME='netresq'
def netresq(a):
    D,mxl=[],'/0'
    get = urllib.request.urlopen("https://bgp.he.net/ip/"+a.rstrip(),None,None)
    html = get.read()
    soup = BeautifulSoup(html,"html.parser")
    fl,A=[],[]
    fl=soup.find_all('td', {'class': 'nowrap'})
    for j in fl:
        j=j.find('a').get('href').split('/')
        D.append(j[2]+'/'+j[3])
    for i in D:
        if int(i.split('/')[1])>int(mxl.split('/')[1]): mxl=i
    return(mxl)
def dnsresq(a):
    D=''
    get = urllib.request.urlopen("https://bgp.he.net/dns/"+a.rstrip()+"#_ipinfo",None,None)
    html = get.read()
    soup = BeautifulSoup(html,"html.parser")
    fl,A=[],[]
    fl=soup.find_all('div',{'class': 'tabdata hidden'}, {'id': 'ipinfo'})
    if fl!=[]:
        fl1=fl[0].find_all('div',{'class':'boundedcontent'})
        for j in fl1:
            j=j.find('a').get('href')
            D=j[4:]
    else: return('203.111.254.0')
    return(D)
def countrycheck():
    with open('14.txt') as f: a=f.readlines()
    D=[]
    for i in tqdm (a, desc="Countrycheck Wait..."):
        if i!='/0':
            get = urllib.request.urlopen(f"https://bgp.he.net/net/{i}",None,None)
            html = get.read()
            soup = BeautifulSoup(html,"html.parser")
            fl=soup.find_all('div',{'class': 'tabdata'}, {'id': 'netinfo'})
            fl1=fl[0].find_all('td')
            for k in fl1:
                if k.find('img') is not None: fli=k.find('img').get('alt')
            D.append([i.rstrip(),fli.rstrip()])
            pass
    for f in D:
        print(f[0],f[1])
