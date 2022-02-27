#合併chosen tsv


# #二和一
# a=open('C:/Users/user/Desktop/生專/python/chosen tsv/202004_01.tsv','r',encoding='utf-8')
# b=open('C:/Users/user/Desktop/生專/python/chosen tsv/202004_02.tsv','r',encoding='utf-8')
# result=open('C:/Users/user/Desktop/生專/python/chosen tsv/202004.tsv','w',encoding='utf-8')
# result.write(a.read())
# result.write(b.read())



# #將兩個同月但有些data不一樣的metadata合併 (沒有重複的)
# # failed
# import csv
# check=open('C:/Users/user/Desktop/生專/python/chosen tsv/202004.tsv','r',encoding='utf-8')
# check_tsv=csv.reader(check,delimiter='\t')
# name_dict=[]
# for line in check_tsv:
#     if line[0] != "seqName":
#         name_dict.append(line[0])
# check.close()

# data=open('C:/Users/user/Desktop/生專/python/chosen tsv/202004_02.tsv','r',encoding='utf-8')
# result=open('C:/Users/user/Desktop/生專/python/chosen tsv/test202004.tsv','w',encoding='utf-8')
# data_tsv=csv.reader(data,delimiter='\t')

# for line in data_tsv:
#     if line[0] in name_dict:
#         l=data.readline()
#         continue
#     else:
#         result.write(data.readline())
# data.close()
# result.close()


#二十個月大合併
#2020
result=open('C:/Users/user/Desktop/生專/python/chosen tsv/all chosen.tsv','w',encoding='utf-8')
for i in range(202002,202014):
    tem=open('C:/Users/user/Desktop/生專/python/chosen tsv/'+str(i)+'.tsv','r',encoding='utf-8')
    c=1
    for line in tem.readlines():
        if c==1 and i!=202002:
            # print(line+'\n')
            c+=1
        else:
            result.write(line)
            # print(c)
            c+=1
    tem.close()
#2021
for i in range(202101,202110):
    tem=open('C:/Users/user/Desktop/生專/python/chosen tsv/'+str(i)+'.tsv','r',encoding='utf-8')
    c=1
    for line in tem.readlines():
        if c==1:
            c+=1
        else:
            result.write(line)
            c+=1
    tem.close()


