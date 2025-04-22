import codecs
fileObj = codecs.open( "1.txt", "r", "utf_8_sig" )
text = fileObj.readlines()
s=0
for i in range(len(text)):
    if text[i].count('TIME_WAIT') or text[i].count('CLOSE_WAIT'):
        while text[i+s].count('TCP')!=0:
            s+=1
        print(text[i],text[s])
        if s==0:
            while text[i+s].count('UDP')!=0:
                s+=1
            print(text[i],text[s])
        s=0
fileObj.close()