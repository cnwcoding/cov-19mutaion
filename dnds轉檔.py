#把dnds原始檔變成csv(excel的)
f_dic={"E","M","N","orf1a","orf1b","orf3a","orf6","orf7a","orf7b","orf8","orf10","S"}
# #單次測試
# old=open('c:/Users/user/Desktop/生專/python/correct dnds(ori)/E/2ML.dN','r')
# new=open('c:/Users/user/Desktop/生專/python/correct dnds/E_dn.csv','w')
# co=old.read()
# new.write(co)
# old.close()
# new.close()

#全部
for f in f_dic:
    old=open('c:/Users/user/Desktop/生專/python/correct dnds(ori)/NEW202107/'+f+'/2ML.dN','r')
    new=open('c:/Users/user/Desktop/生專/python/correct dnds/pre7/pre'+f+'_dn.csv','w')
    co=old.read()
    new.write(co)
    old.close()
    new.close()
    
    old=open('c:/Users/user/Desktop/生專/python/correct dnds(ori)/NEW202107/'+f+'/2ML.dS','r')
    new=open('c:/Users/user/Desktop/生專/python/correct dnds/pre7/pre'+f+'_ds.csv','w')
    co=old.read()
    new.write(co)
    old.close()
    new.close()