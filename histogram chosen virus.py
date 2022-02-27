#把metadata拿去跟nextclade對照
#做出畫病毒種類分布圖的表(名字 種類 月份 地區)
import csv

clade_f = open('C:/Users/user/Desktop/生專/python/find virus type/nextclade.tsv','r',encoding='utf-8')
clade_tsv =csv.reader(clade_f, delimiter="\t")

name_clade_mon_loc_dict={} 

for line in clade_tsv:
    if line[0] != "seqName":
        if line[1] != "":
            name_clade_mon_loc_dict[line[0]] = [line[1]]

metadata_f = open('C:/Users/user/Desktop/生專/python/chosen tsv/all chosen.tsv','r',encoding='utf-8')
metadata_tsv = csv.reader(metadata_f, delimiter="\t")

for line in metadata_tsv:
    if line[0] in name_clade_mon_loc_dict:
        if len(name_clade_mon_loc_dict[line[0]])==1:
            year_mon =line[4][:7]
            name_clade_mon_loc_dict[line[0]].append(year_mon)
            name_clade_mon_loc_dict[line[0]].append(line[7])

new_f = open("name_clade_mon_loc.tsv", "w")
new_f.writelines("seq_name"+'\t'+"clade"+'\t'+"month"+'\t'+"location\n")

for key in name_clade_mon_loc_dict:
    new_line = key+"\t"+"\t".join(name_clade_mon_loc_dict[key])
    new_f.writelines(new_line+"\n")

clade_f.close()
metadata_f.close()
new_f.close()
