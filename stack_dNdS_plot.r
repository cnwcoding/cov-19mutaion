library(ggplot2)
library(ggpubr)
result_table = read.csv("result.tsv",sep = '\t', header = TRUE)
#result_table = read.csv("dSnot0dNdS.tsv",sep = '\t', header = TRUE)
dN_plot = function(result_table,orf_name){
  orf_dN_t = result_table[result_table$ORF == orf_name & result_table$d_WHAT == "dN",]
  
  dN_line_plot <- ggplot(data = orf_dN_t, mapping = aes(x = Month, y = Mean, group = 1)) + geom_line(size = 1)+geom_point()+
    theme(text = element_text(size=10), axis.text.x = element_text(angle=45, hjust=1))
  return(dN_line_plot)
}
dS_plot = function(result_table,orf_name){
  orf_dS_t = result_table[result_table$ORF == orf_name & result_table$d_WHAT == "dS",]

  dS_line_plot <- ggplot(data = orf_dS_t , mapping = aes(x = Month, y = Mean, group = 1)) + geom_line(size = 1)+geom_point()+
    theme(text = element_text(size=10), axis.text.x = element_text(angle=45, hjust=1))
 
  return(dS_line_plot)
}
dNdS_plot = function(result_table,orf_name){
  orf_dNdS_t = result_table[result_table$ORF == orf_name & result_table$d_WHAT == "dNdS",]
  
  dNdS_line_plot <- ggplot(data = orf_dNdS_t, mapping = aes(x = Month, y = Mean, group = 1)) + geom_line(size = 1)+geom_point()+
    theme(text = element_text(size=10), axis.text.x = element_text(angle=40, hjust=1))
  return(dNdS_line_plot)
}
#orf_name_list = c("orf1a","orf1b","orf3a","orf6","orf7a","orf7b","orf8","E","M","N","S","orf10")
orf1a_dN_plot = dN_plot(result_table, "orf1a")
orf1b_dN_plot = dN_plot(result_table, "orf1b")
orf3a_dN_plot = dN_plot(result_table, "orf3a")
orf6_dN_plot = dN_plot(result_table, "orf6")
orf7a_dN_plot = dN_plot(result_table, "orf7a")
orf7b_dN_plot = dN_plot(result_table, "orf7b")
orf8_dN_plot = dN_plot(result_table, "orf8")
orf10_dN_plot = dN_plot(result_table, "orf10")
E_dN_plot = dN_plot(result_table, "E")
M_dN_plot = dN_plot(result_table, "M")
N_dN_plot = dN_plot(result_table, "N")
S_dN_plot = dN_plot(result_table, "S")

stack_dN = ggarrange(orf1a_dN_plot+ rremove("x.text")+ rremove("xlab")+ rremove("ylab"),orf1b_dN_plot+ rremove("x.text")+ rremove("xlab")+ rremove("ylab"),
                     orf3a_dN_plot+ rremove("x.text")+ rremove("xlab")+ rremove("ylab"),orf6_dN_plot+ rremove("x.text")+ rremove("xlab")+ rremove("ylab"),
                     orf7a_dN_plot+ rremove("x.text")+ rremove("xlab")+ rremove("ylab"),orf7b_dN_plot+ rremove("x.text")+ rremove("xlab")+ rremove("ylab"),
                     orf8_dN_plot+ rremove("x.text")+ rremove("xlab")+ rremove("ylab"),orf10_dN_plot+ rremove("x.text")+ rremove("xlab")+ rremove("ylab"),
                     E_dN_plot+ rremove("x.text")+ rremove("xlab")+ rremove("ylab"),M_dN_plot+ rremove("x.text")+ rremove("xlab")+ rremove("ylab"),
                     N_dN_plot+ rremove("xlab")+ rremove("ylab"),S_dN_plot+ rremove("xlab")+ rremove("ylab"),
                     labels = c("ORF1a","ORF1b","ORF3a","ORF6","ORF7a","ORF7b","ORF8","ORF10","E","M","N","S"),
                     label.x = c(0.1,0.1,0.1,0.125,0.1,0.1,0.125,0.11,0.2,0.2,0.2,0.2), 
                     label.y = 0.95, 
                     font.label = list(size = 10, face = "bold"),
                     ncol = 2, nrow = 6)
stack_dN = annotate_figure(stack_dN,
                           top = text_grob("Non-synonymous substitution rate(dN)", face = "bold",  size = 16),
                           bottom = text_grob("Year-month", face = "bold", size = 14),
                           left = text_grob("Monthly average dN", face = "bold", rot = 90, size= 14),
)
stack_dN
remove(stack_dN)


orf1a_dS_plot = dS_plot(result_table, "orf1a")
orf1b_dS_plot = dS_plot(result_table, "orf1b")
orf3a_dS_plot = dS_plot(result_table, "orf3a")
orf6_dS_plot = dS_plot(result_table, "orf6")
orf7a_dS_plot = dS_plot(result_table, "orf7a")
orf7b_dS_plot = dS_plot(result_table, "orf7b")
orf8_dS_plot = dS_plot(result_table, "orf8")
orf10_dS_plot = dS_plot(result_table, "orf10")
E_dS_plot = dS_plot(result_table, "E")
M_dS_plot = dS_plot(result_table, "M")
N_dS_plot = dS_plot(result_table, "N")
S_dS_plot = dS_plot(result_table, "S")

stack_dS = ggarrange(orf1a_dS_plot+ rremove("x.text")+ rremove("xlab")+ rremove("ylab"),orf1b_dS_plot+ rremove("x.text")+ rremove("xlab")+ rremove("ylab"),
                     orf3a_dS_plot+ rremove("x.text")+ rremove("xlab")+ rremove("ylab"),orf6_dS_plot+ rremove("x.text")+ rremove("xlab")+ rremove("ylab"),
                     orf7a_dS_plot+ rremove("x.text")+ rremove("xlab")+ rremove("ylab"),orf7b_dS_plot+ rremove("x.text")+ rremove("xlab")+ rremove("ylab"),
                     orf8_dS_plot+ rremove("x.text")+ rremove("xlab")+ rremove("ylab"),orf10_dS_plot+ rremove("x.text")+ rremove("xlab")+ rremove("ylab"),
                     E_dS_plot+ rremove("x.text")+ rremove("xlab")+ rremove("ylab"),M_dS_plot+ rremove("x.text")+ rremove("xlab")+ rremove("ylab"),
                     N_dS_plot+ rremove("xlab")+ rremove("ylab"),S_dS_plot+ rremove("xlab")+ rremove("ylab"),
                     labels = c("ORF1a","ORF1b","ORF3a","ORF6","ORF7a","ORF7b","ORF8","ORF10","E","M","N","S"),
                     label.x = c(0.1,0.1,0.1,0.125,0.1,0.1,0.125,0.11,0.2,0.2,0.2,0.2), 
                     label.y = 0.95, 
                     font.label = list(size = 10, face = "bold"),
                     ncol = 2, nrow = 6)
stack_dS = annotate_figure(stack_dS,
                           top = text_grob("Synonymous substitution rate(dS)", face = "bold",  size = 16),
                           bottom = text_grob("Year-month", face = "bold", size = 14),
                           left = text_grob("Monthly average dS", face = "bold", rot = 90, size= 14),
)
stack_dS
remove(stack_dS)


orf1a_dNdS_plot = dNdS_plot(result_table, "orf1a")
orf1b_dNdS_plot = dNdS_plot(result_table, "orf1b")
orf3a_dNdS_plot = dNdS_plot(result_table, "orf3a")
orf6_dNdS_plot = dNdS_plot(result_table, "orf6")
orf7a_dNdS_plot = dNdS_plot(result_table, "orf7a")
orf7b_dNdS_plot = dNdS_plot(result_table, "orf7b")
orf8_dNdS_plot = dNdS_plot(result_table, "orf8")
orf10_dNdS_plot = dNdS_plot(result_table, "orf10")
E_dNdS_plot = dNdS_plot(result_table, "E")
M_dNdS_plot = dNdS_plot(result_table, "M")
N_dNdS_plot = dNdS_plot(result_table, "N")
S_dNdS_plot = dNdS_plot(result_table, "S")

stack_dNdS = ggarrange(orf1a_dNdS_plot+ rremove("xlab")+ rremove("ylab"),orf1b_dNdS_plot+ rremove("xlab")+ rremove("ylab"),
                       orf3a_dNdS_plot+ rremove("xlab")+ rremove("ylab"),orf6_dNdS_plot+ rremove("xlab")+ rremove("ylab"),
                       orf7a_dNdS_plot+ rremove("xlab")+ rremove("ylab"),orf7b_dNdS_plot+ rremove("xlab")+ rremove("ylab"),
                       orf8_dNdS_plot+ rremove("xlab")+ rremove("ylab"),orf10_dNdS_plot+ rremove("xlab")+ rremove("ylab"),
                       E_dNdS_plot+ rremove("xlab")+ rremove("ylab"),M_dNdS_plot+ rremove("xlab")+ rremove("ylab"),
                       N_dNdS_plot+ rremove("xlab")+ rremove("ylab"),S_dNdS_plot+ rremove("xlab")+ rremove("ylab"),
                       labels = c("ORF1a","ORF1b","ORF3a","ORF6","ORF7a","ORF7b","ORF8","ORF10","E","M","N","S"),
                       label.x = c(0.1,0.1,0.1,0.125,0.1,0.1,0.125,0.11,0.2,0.2,0.2,0.2), 
                       label.y = 0.95, 
                       font.label = list(size = 10, face = "bold"),
                       ncol = 2, nrow = 6)
stack_dNdS = annotate_figure(stack_dNdS,
                             top = text_grob("dN/dS Ratio", face = "bold",  size = 16),
                             #top = text_grob("dN/dS Ratio(only dS > 0)", face = "bold",  size = 16),
                             bottom = text_grob("Year-month", face = "bold", size = 14),
                             left = text_grob("Monthly average dN/dS", face = "bold", rot = 90, size= 14),
)
stack_dNdS
remove(stack_dNdS)