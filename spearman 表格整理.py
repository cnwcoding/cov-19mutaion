import pandas as pd

#result=open('c:/Users/user/Desktop/生專/spearman/all_spearman.tsv','w')
f_dic = ["ORF1a","ORF1b","S","ORF3a","E","M","ORF6","ORF7a","ORF7b","ORF8","N","ORF10"]
df_all=pd.DataFrame({})
for f in range(0,12) :
    file=open('c:/Users/user/Desktop/生專/spearman/'+f_dic[f]+'_Ka_byclade.tsv','r')
    csvf=pd.read_csv(file,delimiter='\t')
    cf=csvf.sort_values(by='position')
    checkedf=cf['spearman_cc']<0
    df=pd.DataFrame(cf[checkedf])
    s=[]
    for i in range(0,len(df.index)):
        s.append(f_dic[f])
    df.insert(0,column='fraction',value=s)
    dff=df[['clade','fraction','position','N_note',]]
    df_all=pd.concat([df_all,dff])
    file.close()

df_all.to_csv('c:/Users/user/Desktop/生專/spearman/all_spearman負相關.tsv',index=None,sep='\t')

# for line in cff:
    # print(line)
    #if line[5]<0:
        # print(line[1]+'\n')

