#去換行符
seq=open('202103ori.fasta','r')  #這裡放要處理的檔案的檔名
n=open('done seq.txt','w')  #這個是處理好的
a='\n'
b=0
for line in seq.readlines():
    if line.startswith('>')==False :                          
        line = line.strip()
    else :
        b+=1
        if(b>2):
            line=a+line
    if (b>1):   
        n.write(line)
