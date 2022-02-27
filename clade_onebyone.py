import csv
import re
import numpy as np
import rpy2.robjects as robjects

def trendline(index,data, order=1):
    coeffs = np.polyfit(index, list(data), order)
    slope = coeffs[-2]
    return float(slope)
"""
分开研究每个clade中的突变是否随时间月份增加
从nextclade.tsv得到每个clade分别有哪些seq，metadata得到每个seq年月
"""
def clade_onebyone(orf_name):
	rcortest = robjects.r("cor.test")

	codon_table = {
	'ATA':'I', 'ATC':'I', 'ATT':'I', 'ATG':'M',
	'ACA':'T', 'ACC':'T', 'ACG':'T', 'ACT':'T',
	'AAC':'N', 'AAT':'N', 'AAA':'K', 'AAG':'K',
	'AGC':'S', 'AGT':'S', 'AGA':'R', 'AGG':'R',
	'CTA':'L', 'CTC':'L', 'CTG':'L', 'CTT':'L',
	'CCA':'P', 'CCC':'P', 'CCG':'P', 'CCT':'P',
	'CAC':'H', 'CAT':'H', 'CAA':'Q', 'CAG':'Q',
	'CGA':'R', 'CGC':'R', 'CGG':'R', 'CGT':'R',
	'GTA':'V', 'GTC':'V', 'GTG':'V', 'GTT':'V',
	'GCA':'A', 'GCC':'A', 'GCG':'A', 'GCT':'A',
	'GAC':'D', 'GAT':'D', 'GAA':'E', 'GAG':'E',
	'GGA':'G', 'GGC':'G', 'GGG':'G', 'GGT':'G',
	'TCA':'S', 'TCC':'S', 'TCG':'S', 'TCT':'S',
	'TTC':'F', 'TTT':'F', 'TTA':'L', 'TTG':'L',
	'TAC':'Y', 'TAT':'Y', 'TAA':'_', 'TAG':'_',
	'TGC':'C', 'TGT':'C', 'TGA':'_', 'TGG':'W',
	}

	nuc_f = open(orf_name+"_rmvfin.fasta","r")

	nuc_line_list = nuc_f.readlines()

	first_seq = nuc_line_list[1]
	other_nuc = nuc_line_list[2:]


	clade_f = open("nextclade.tsv","r")
	clade_tsv = csv.reader(clade_f, delimiter="\t")

	name_clade_mon_seq_dict = {} #name_clade_mon_seq_dict下每个seq名字对应一个列表[clade,month,sequence]
	clade_permon_dict = {}

	Ka_dict = {}
	Ks_dict = {}

	for line in clade_tsv:
		if line[0] != "seqName":
			if line[1] != "":
				name_clade_mon_seq_dict[line[0]] = [line[1]]
				if clade_permon_dict.__contains__(line[1]):
					pass
				else:
					clade_permon_dict[line[1]] = [0]*20
					Ka_dict[line[1]] = {}
					Ks_dict[line[1]] = {}


	metadata_f = open("USA_202001202108_metadata.tsv","r")
	metadata_tsv = csv.reader(metadata_f, delimiter="\t")

	for line_list in metadata_tsv:
		if line_list[0] in name_clade_mon_seq_dict:
			year_mon = line_list[4][:7]
			name_clade_mon_seq_dict[line_list[0]].append(year_mon)

	for i in range(len(other_nuc)):
		if other_nuc[i].startswith(">"):
			name = other_nuc[i][1:].strip()
			if name in name_clade_mon_seq_dict:
				seq = other_nuc[i+1].strip()
				name_clade_mon_seq_dict[name].append(seq)

	nuc_f.close()

	month_order_list = ["2020-01","2020-02","2020-03","2020-04","2020-05","2020-06","2020-07","2020-08","2020-09","2020-10","2020-11","2020-12","2021-01","2021-02","2021-03","2021-04","2021-05","2021-06","2021-07","2021-08"]
	mon_index = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]

	for m in range(len(month_order_list)):
		for name in name_clade_mon_seq_dict:
			if name_clade_mon_seq_dict[name][1] == month_order_list[m]:
				clade_permon_dict[name_clade_mon_seq_dict[name][0]][m] += 1

	Ka_new_csv = open(orf_name+"_Ka_byclade.tsv","w")

	Ka_title_list = ["clade","position","ref_AA","mutation","N_note","spearman_cc","spearman_p","slope","mutation_proportion"]
	Ka_title = "\t".join(Ka_title_list)
	Ka_new_csv.writelines(Ka_title+"\n")

	Ks_new_csv = open(orf_name+"_Ks_byclade.tsv","w")

	Ks_title_list = ["clade","position","ref_NT","mutation","S_note","spearman_cc","spearman_p","slope","mutation_proportion"]
	Ks_title = "\t".join(Ks_title_list)
	Ks_new_csv.writelines(Ks_title+"\n")

	for m in range(len(month_order_list)):
		for name in name_clade_mon_seq_dict:
			mon =  name_clade_mon_seq_dict[name][1]
			if mon == month_order_list[m]:
				clade = name_clade_mon_seq_dict[name][0]
				seq = name_clade_mon_seq_dict[name][2]
				if len(seq)%3 == 0:
					for i in range(0, len(seq), 3):
						seq_codon = seq[i:i+3]
						if re.findall(r'[^ATCG]', seq_codon, flags = re.IGNORECASE):
							pass
						else:
							template_codon = first_seq[i:i+3]
							if seq_codon == template_codon:
								pass
							elif re.findall(r'[^ATCG]', template_codon, flags = re.IGNORECASE):
								pass
							else:
								if codon_table[seq_codon] != codon_table[template_codon]:
									pre_note = codon_table[template_codon]+str(int(i/3)+1)
									N_note = codon_table[template_codon]+str(int(i/3)+1)+codon_table[seq_codon]
									if Ka_dict[clade].__contains__(pre_note):
										if Ka_dict[clade][pre_note].__contains__(N_note):
											Ka_dict[clade][pre_note][N_note][m] += 1
										else:
											Ka_dict[clade][pre_note][N_note] = [0]*20
											Ka_dict[clade][pre_note][N_note][m] += 1
									else:
										Ka_dict[clade][pre_note] = {}
										Ka_dict[clade][pre_note][N_note] = [0]*20
										Ka_dict[clade][pre_note][N_note][m] += 1

								elif codon_table[seq_codon] == codon_table[template_codon]:
									pre_note = template_codon+str(int(i/3)+1)
									S_note = template_codon+str(int(i/3)+1)+seq_codon
									if Ks_dict[clade].__contains__(pre_note):
										if Ks_dict[clade][pre_note].__contains__(S_note):
											Ks_dict[clade][pre_note][S_note][m] += 1
										else:
											Ks_dict[clade][pre_note][S_note] = [0]*20
											Ks_dict[clade][pre_note][S_note][m] += 1
									else:
										Ks_dict[clade][pre_note] = {}
										Ks_dict[clade][pre_note][S_note] = [0]*20
										Ks_dict[clade][pre_note][S_note][m] += 1


	for clade in Ka_dict:
		for pre in Ka_dict[clade]:
			for N in Ka_dict[clade][pre]:
				for m in range(len(month_order_list)):
					if clade_permon_dict[clade][m] != 0:
						Ka_dict[clade][pre][N][m] = Ka_dict[clade][pre][N][m]/clade_permon_dict[clade][m]
					else:
						Ka_dict[clade][pre][N][m] = 0

	for clade in Ka_dict:
		for pre in Ka_dict[clade]:
			for N in Ka_dict[clade][pre]:
				temp_index = []
				temp_clade = []
				for m in range(len(month_order_list)):
					if Ka_dict[clade][pre][N][m] == 0:
						pass
					else:
						temp_index.append(mon_index[m])
						temp_clade.append(Ka_dict[clade][pre][N][m])
						
				if len(temp_index) >= 2:
					r_index = robjects.FloatVector(temp_index)
					r_clade = robjects.FloatVector(temp_clade)
					cor_result = rcortest(r_index, r_clade,method = "s")
					Ka_spearman = cor_result[cor_result.names.index("estimate")][0]
					Ka_pvalue = cor_result[cor_result.names.index("p.value")][0]
					if Ka_pvalue <= 0.05:
						trend_slope = trendline(temp_index,temp_clade)
						Ka_newline_list = [clade,pre[1:],pre[0],N[-1],N,str(Ka_spearman),str(Ka_pvalue),str(trend_slope),str(temp_clade)]
						Ka_newline = "\t".join(Ka_newline_list)
						Ka_new_csv.writelines(Ka_newline+"\n")

	
	for clade in Ks_dict:
		for pre in Ks_dict[clade]:
			for S in Ks_dict[clade][pre]:
				for m in range(len(month_order_list)):
					if clade_permon_dict[clade][m] != 0:
						Ks_dict[clade][pre][S][m] = Ks_dict[clade][pre][S][m]/clade_permon_dict[clade][m]
					else:
						Ks_dict[clade][pre][S][m] = 0

	for clade in Ks_dict:
		for pre in Ks_dict[clade]:
			for S in Ks_dict[clade][pre]:
				temp_index = []
				temp_clade = []
				for m in range(len(month_order_list)):
					if Ks_dict[clade][pre][S][m] == 0:
						pass
					else:
						temp_index.append(mon_index[m])
						temp_clade.append(Ks_dict[clade][pre][S][m])
						
				if len(temp_index) >= 2:
					r_index = robjects.FloatVector(temp_index)
					r_clade = robjects.FloatVector(temp_clade)
					cor_result = rcortest(r_index, r_clade,method = "s")
					Ks_spearman = cor_result[cor_result.names.index("estimate")][0]
					Ks_pvalue = cor_result[cor_result.names.index("p.value")][0]
					if Ks_pvalue <= 0.05:
						trend_slope = trendline(temp_index,temp_clade)
						Ks_newline_list = [clade,pre[3:],pre[:3],S[-3:],S,str(Ks_spearman),str(Ks_pvalue),str(trend_slope),str(temp_clade)]
						Ks_newline = "\t".join(Ks_newline_list)
						Ks_new_csv.writelines(Ks_newline+"\n")


	metadata_f.close()

	return(True)


#orf_name_list = ["orf1a","orf1b","orf3a","orf6","orf7a","orf7b","orf8","envelope","matrix","nucleocapsid","spike","orf10"]
#orf_name_list = ["orf1a","orf1b","nucleocapsid","spike"]
orf_name_list = ["orf6","orf7a","orf7b","orf8","envelope","matrix","orf10"]

for orf in orf_name_list:
	clade_onebyone(orf)
