#for finding the missing metadata(202012)

import csv

clade_f= open('C:/Users/user/Desktop/生專/python/chosen tsv/name_clade_mon_loc.tsv','r',encoding='utf-8')
clade_tsv =csv.reader(clade_f, delimiter="\t")
done=open('C:/Users/user/Desktop/生專/python/find virus type/clade_meta_search.tsv','w',encoding='utf-8')
x=0
for line in clade_tsv:
    # if line[0]=="hCoV-19/England/NORW-F6674/2020":
        # x+=1
    # elif line[0]=="hCoV-19/England/QEUH-DD3977/2021":
        # break

    if line[1]=="England":
        done.write(line[0]+'\n')

