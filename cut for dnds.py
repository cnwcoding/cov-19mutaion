# 切割 分析(dnds)
#seq=open('c:/Users/user/Desktop/生專/python/done_seq/202005done seq.txt','r')    #開要切的檔案
#well=open('well value seq.txt','w')     #切完的檔案

y=0
z=3
a=open('c:/Users/user/Desktop/生專/python/cut for dnds(combine)/ORF1a.txt','w')
b=open('c:/Users/user/Desktop/生專/python/cut for dnds(combine)/ORF1b.txt','w')
c=open('c:/Users/user/Desktop/生專/python/cut for dnds(combine)/S.txt','w')
d=open('c:/Users/user/Desktop/生專/python/cut for dnds(combine)/ORF3a.txt','w')
e=open('c:/Users/user/Desktop/生專/python/cut for dnds(combine)/E.txt','w')
f=open('c:/Users/user/Desktop/生專/python/cut for dnds(combine)/M.txt','w')
g=open('c:/Users/user/Desktop/生專/python/cut for dnds(combine)/ORF6.txt','w')
h=open('c:/Users/user/Desktop/生專/python/cut for dnds(combine)/ORF7a.txt','w')
i=open('c:/Users/user/Desktop/生專/python/cut for dnds(combine)/ORF7b.txt','w')
j=open('c:/Users/user/Desktop/生專/python/cut for dnds(combine)/ORF8.txt','w')
k=open('c:/Users/user/Desktop/生專/python/cut for dnds(combine)/N.txt','w')
l=open('c:/Users/user/Desktop/生專/python/cut for dnds(combine)/ORF10.txt','w')

for month in range (202002,202022):
    x=0 #算次數(200次)
    tem=str(month)
    seq=open('c:/Users/user/Desktop/生專/python/done_seq/'+tem+'done seq.txt','r')
    for line in seq.readlines():
        if x>=200:
            break
        if line.startswith('>')==False: 
            ORF1a=line[265:13483]   #第266個到13483
            ORF1b=line[13767:21555]
            S=line[21562:25384]
            ORF3a=line[25392:26220]
            E=line[26244:26472]
            M=line[26522:27191]
            ORF6=line[27201:27387]
            ORF7a=line[27393:27759]
            ORF7b=line[27755:27887]
            ORF8=line[27893:28259]
            N=line[28273:29533]
            ORF10=line[29557:29674]

            count=len(ORF1a)
            s=ORF1a
            y=0
            z=3
            while z<(len(s)-2):
                if s[y:z]=='taa' or s[y:z]=='tag' or s[y:z]=='tga':
                    s=s.replace(s,s[0:y]+'---'+s[z:])
                y=z
                z=z+3
            s=s.replace("a","").replace("t","").replace("c","").replace("g","")
            if len(s)/count>=0.05:
                continue
            s=s.replace("-","")
            if len(s)!=0:
                continue

            count=len(ORF1b)
            s=ORF1b
            y=0
            z=3
            while z<(len(s)-2):
                if s[y:z]=='taa' or s[y:z]=='tag' or s[y:z]=='tga':
                    s=s.replace(s,s[0:y]+'---'+s[z:])
                y=z
                z=z+3
            s=s.replace("a","").replace("t","").replace("c","").replace("g","")
            if len(s)/count>=0.05:
                continue
            s=s.replace("-","")
            if len(s)!=0:
                continue

            count=len(S)
            s=S
            y=0
            z=3
            while z<(len(s)-2):
                if s[y:z]=='taa' or s[y:z]=='tag' or s[y:z]=='tga':
                    s=s.replace(s,s[0:y]+'---'+s[z:])
                y=z
                z=z+3
            s=s.replace("a","").replace("t","").replace("c","").replace("g","")
            if len(s)/count>=0.05:
                continue
            s=s.replace("-","")
            if len(s)!=0:
                continue

            count=len(ORF3a)
            s=ORF3a
            y=0
            z=3
            while z<(len(s)-2):
                if s[y:z]=='taa' or s[y:z]=='tag' or s[y:z]=='tga':
                    s=s.replace(s,s[0:y]+'---'+s[z:])
                y=z
                z=z+3
            s=s.replace("a","").replace("t","").replace("c","").replace("g","")
            if len(s)/count>=0.05:
                continue
            s=s.replace("-","")
            if len(s)!=0:
                continue

            count=len(E)
            s=E
            y=0
            z=3
            while z<(len(s)-2):
                if s[y:z]=='taa' or s[y:z]=='tag' or s[y:z]=='tga':
                    s=s.replace(s,s[0:y]+'---'+s[z:])
                y=z
                z=z+3
            s=s.replace("a","").replace("t","").replace("c","").replace("g","")
            if len(s)/count>=0.05:
                continue
            s=s.replace("-","")
            if len(s)!=0:
                continue

            count=len(M)
            s=M
            y=0
            z=3
            while z<(len(s)-2):
                if s[y:z]=='taa' or s[y:z]=='tag' or s[y:z]=='tga':
                    s=s.replace(s,s[0:y]+'---'+s[z:])
                y=z
                z=z+3
            s=s.replace("a","").replace("t","").replace("c","").replace("g","")
            if len(s)/count>=0.05:
                continue
            s=s.replace("-","")
            if len(s)!=0:
                continue

            count=len(ORF6)
            s=ORF6
            y=0
            z=3
            while z<(len(s)-2):
                if s[y:z]=='taa' or s[y:z]=='tag' or s[y:z]=='tga':
                    s=s.replace(s,s[0:y]+'---'+s[z:])
                y=z
                z=z+3
            s=s.replace("a","").replace("t","").replace("c","").replace("g","")
            if len(s)/count>=0.05:
                continue
            s=s.replace("-","")
            if len(s)!=0:
                continue

            count=len(ORF7a)
            s=ORF7a
            y=0
            z=3
            while z<(len(s)-2):
                if s[y:z]=='taa' or s[y:z]=='tag' or s[y:z]=='tga':
                    s=s.replace(s,s[0:y]+'---'+s[z:])
                y=z
                z=z+3
            s=s.replace("a","").replace("t","").replace("c","").replace("g","")
            if len(s)/count>=0.05:
                continue
            s=s.replace("-","")
            if len(s)!=0:
                continue

            count=len(ORF7b)
            s=ORF7b
            y=0
            z=3
            while z<(len(s)-2):
                if s[y:z]=='taa' or s[y:z]=='tag' or s[y:z]=='tga':
                    s=s.replace(s,s[0:y]+'---'+s[z:])
                y=z
                z=z+3
            s=s.replace("a","").replace("t","").replace("c","").replace("g","")
            if len(s)/count>=0.05:
                continue
            s=s.replace("-","")
            if len(s)!=0:
                continue

            count=len(ORF8)
            s=ORF8
            y=0
            z=3
            while z<(len(s)-2):
                if s[y:z]=='taa' or s[y:z]=='tag' or s[y:z]=='tga':
                    s=s.replace(s,s[0:y]+'---'+s[z:])
                y=z
                z=z+3
            s=s.replace("a","").replace("t","").replace("c","").replace("g","")
            if len(s)/count>=0.05:
                continue
            s=s.replace("-","")
            if len(s)!=0:
                continue

            count=len(N)
            s=N
            y=0
            z=3
            while z<(len(s)-2):
                if s[y:z]=='taa' or s[y:z]=='tag' or s[y:z]=='tga':
                    s=s.replace(s,s[0:y]+'---'+s[z:])
                y=z
                z=z+3
            s=s.replace("a","").replace("t","").replace("c","").replace("g","")
            if len(s)/count>=0.05:
                continue
            s=s.replace("-","")
            if len(s)!=0:
                continue

            count=len(ORF10)
            s=ORF10
            y=0
            z=3
            while z<(len(s)-2):
                if s[y:z]=='taa' or s[y:z]=='tag' or s[y:z]=='tga':
                    s=s.replace(s,s[0:y]+'---'+s[z:])
                y=z
                z=z+3
            s=s.replace("a","").replace("t","").replace("c","").replace("g","")
            if len(s)/count>=0.05:
                continue
            s=s.replace("-","")
            if len(s)!=0:
                continue

            #print(x) 檢查次數的
            if(x > 0):
                a.write('\n')
                b.write('\n')
                c.write('\n')
                d.write('\n')
                e.write('\n')
                f.write('\n')
                g.write('\n')
                h.write('\n')
                i.write('\n')
                j.write('\n')
                k.write('\n')
                l.write('\n')

            a.write(name)
            b.write(name)
            c.write(name)
            d.write(name)
            e.write(name)
            f.write(name)
            g.write(name)
            h.write(name)
            i.write(name)
            j.write(name)
            k.write(name)
            l.write(name)
            #well.write(name)

            a.write(ORF1a[0:len(ORF1a)-3])
            b.write(ORF1b[0:len(ORF1b)-3])
            c.write(S[0:len(S)-3])
            d.write(ORF3a[0:len(ORF3a)-3])
            e.write(E[0:len(E)-3])
            f.write(M[0:len(M)-3])
            g.write(ORF6[0:len(ORF6)-3])
            h.write(ORF7a[0:len(ORF7a)-3])
            i.write(ORF7b[0:len(ORF7b)-3])
            j.write(ORF8[0:len(ORF8)-3])
            k.write(N[0:len(N)-3])
            l.write(ORF10[0:len(ORF10)-3])
            #well.write(line)
            x+=1
        else:
            name=line[5:]
    #print(x,'\n') #算每個月的病毒數量


    a.write('\n')
    b.write('\n')
    c.write('\n')
    d.write('\n')
    e.write('\n')
    f.write('\n')
    g.write('\n')
    h.write('\n')
    i.write('\n')
    j.write('\n')
    k.write('\n')
    l.write('\n')    

a.close()
b.close()
c.close()
d.close()
e.close()
f.close()
g.close()
h.close()
i.close()
j.close()
k.close()
l.close()  