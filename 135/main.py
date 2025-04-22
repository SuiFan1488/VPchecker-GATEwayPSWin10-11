from tqdm import tqdm
import addrt,_135,netresq
def log(a):
    if a!='0': return(True)
    else: return(False)
def useterminal():
    m=log(input('countrycheck?'))
    F=open('a.txt','w')
    with open('terminal.txt','r') as f:
        a=f.readlines()
    for i in tqdm (a, desc="Loading..."):
        i=i.split()
        if i[3]!='ESTABLISHED':
            F.write('1 '+i[2].split(':')[0]+'\n')
        pass
    F.close()
    addrt.main(m)
print('programscenario:')
a=input()
if a=="terminal": useterminal()
elif a=='countrycheckonly': netresq.countrycheck()
elif a=='zc': _135.callzeroargs(input(("interface: ")))
elif a=='callbyfilename': _135.call(input('Filename:')+'.txt',input(("interface: ")))
elif a=='dc': _135.deletecall('1488.txt')
elif a=='noterm': addrt.noterm(log(input('countrycheck?')))
elif a=='nocheck': addrt.nocheck(log(input('countrycheck?')))