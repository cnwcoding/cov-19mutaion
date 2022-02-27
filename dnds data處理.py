##第一行不要 只要前兩欄 並插入新的dnds(2006/2107)
import csv
import os

f_dic = {"E","M","N","orf1a","orf1b","orf3a","orf6","orf7a","orf7b","orf8","orf10","S"}

for f in f_dic :
#dn
    file = open('c:/Users/user/Desktop/生專/python/correct dnds/pre_done/pre'+f+'_dn.csv','r')
    done = open('c:/Users/user/Desktop/生專/python/correct dnds/done/'+f+'dN.csv','w')
    afile = open('c:/Users/user/Desktop/生專/python/correct dnds/pre6_done/pre'+f+'_dn.csv','r')
    bfile = open('c:/Users/user/Desktop/生專/python/correct dnds/pre7_done/pre'+f+'_dn.csv','r')

    x=1
    fcsv=csv.reader(file)
    acsvf=csv.reader(afile)
    bcsvf=csv.reader(bfile)
    acsv=list(acsvf)
    bcsv=list(bcsvf)
    for line in fcsv:
        if line[0]=="3814":
            continue
        if line[0]=="hCoV-19/Unitedkingdom/consensus":
            done.write(","+line[0]+"\n")
        elif x>614 and x<815:
            done.write(acsv[x-613][0]+","+acsv[x-613][1]+'\n')      #202006的新dnds
        elif x>3214 and x<3415:
            done.write(bcsv[x-3213][0]+","+bcsv[x-3213][1]+'\n')       #202107的新dnds
        else:
            done.write(line[0]+","+line[1]+'\n')
        x+=1

    file.close()
    done.close()
    afile.close()
    bfile.close()

#ds
    file=open('c:/Users/user/Desktop/生專/python/correct dnds/pre_done/pre'+f+'_ds.csv','r')
    done=open('c:/Users/user/Desktop/生專/python/correct dnds/done/'+f+'dS.csv','w')
    afile=open('c:/Users/user/Desktop/生專/python/correct dnds/pre6_done/pre'+f+'_ds.csv','r')
    bfile=open('c:/Users/user/Desktop/生專/python/correct dnds/pre7_done/pre'+f+'_ds.csv','r')

    x=1
    fcsv=csv.reader(file)
    acsvf=csv.reader(afile)
    bcsvf=csv.reader(bfile)
    acsv=list(acsvf)
    bcsv=list(bcsvf)
    for line in fcsv:
        if line[0]=="3814":
            continue
        if line[0]=="hCoV-19/Unitedkingdom/consensus":
            done.write(","+line[0]+"\n")
        elif x>614 and x<815:
            done.write(acsv[x-613][0]+","+acsv[x-613][1]+'\n')      #202006的新dnds
        elif x>3214 and x<3415:
            done.write(bcsv[x-3213][0]+","+bcsv[x-3213][1]+'\n')       #202107的新dnds
        else:
            done.write(line[0]+","+line[1]+'\n')
        x+=1

    file.close()
    done.close()
    afile.close()
    bfile.close()