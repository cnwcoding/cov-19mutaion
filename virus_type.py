# 做總fasta檔 (原始序列)
# 會丟到nextclade 
# 用來找每種病毒每月的比例

# 合併所有chosen fasta
x=open('C:/Users/user/Desktop/生專/python/find virus type/all chosen fasta.fasta','w')
for month in range(202002,202022):
    tem=str(month)
    seqf=open( 'C:/Users/user/Desktop/生專/python/chosen fasta/'+tem+ 'chosen.fasta','r')
    s=seqf.read()
    x.write(s)
    seqf.close()
x.close()
#比對
# y=open('C:/Users/user/Desktop/生專/python/cut for all(combine)/text0.txt','r')
# x=open('C:/Users/user/Desktop/生專/python/cut for all(combine)/text1.txt','r')
# done=open('C:/Users/user/Desktop/生專/python/find virus type/test.fasta','w')
y=open('C:/Users/user/Desktop/生專/python/cut for all(combine)/ORF10.txt','r')  #all done seq (5萬多)(有挑過的)
x=open('C:/Users/user/Desktop/生專/python/find virus type/all chosen fasta.fasta','r')  #all chosen fasta (當初下的每月5000)原始
done=open('C:/Users/user/Desktop/生專/python/find virus type/select chosen fasta.fasta','w')    #最後要的 所有選出使用的seq的原始fasta

select_lines = y.readlines()
select_names = []
for line in select_lines:
    if line.startswith("h"):
        select_names.append(line.strip())

all_lines = x.readlines()


namedict={}
for line in all_lines:
    if line.startswith(">"):
        name=line.strip()
        namedict[name]=""
    else:
        namedict[name]+=line
for name in namedict:
    if name[1:] in select_names:
        done.write(name+"\n")
        done.write(namedict[name])



