#載病毒檔案的隨機篩選(選5000個)
import random
virus=open('cov202103all.csv','r')
v_name=virus.readlines()
chosen_virus=open('chosenvirus.csv','w')
for line in random.sample(v_name,5000):
    chosen_virus.write(line)