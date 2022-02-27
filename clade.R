library(ggplot2)
library(plyr)
library(dplyr)

virus=read.csv("name_clade_mon_loc.tsv",header=TRUE,sep = "\t")

clade_num=ddply(virus,.(clade,month),summarize,number=length(clade))

clade_prop=group_by(clade_num,month)%>%mutate(percent=number/sum(number)*100)

ggplot(clade_prop,aes(x=month,y=percent,fill=clade))+
  geom_bar(colour="black",size=0.1,stat = "identity")+
  labs(title="Proportion of viruses",x="month")+
  theme(axis.text.x=element_text(angle=45,hjust=1))

