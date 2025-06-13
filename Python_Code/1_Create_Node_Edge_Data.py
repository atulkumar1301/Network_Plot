from pathlib import Path
from pathlib import PurePath

source_dir = Path('/Users/akumar/Library/CloudStorage/OneDrive-UniversityofEasternFinland/Projects/Minna/TPM1/')

files = sorted (source_dir.glob('*.txt'))

f_m = open ('/Users/akumar/Library/CloudStorage/OneDrive-UniversityofEasternFinland/Projects/Minna/1_Node_Edge.txt', 'w', 1)
f_m.write ("Target_Gene" + "\t" + "DE_Gene" + "\t" + "RNA_Log2FC" + "\t" + "PRTB_Log2FC" + "\n")

f_m_1 = open ('/Users/akumar/Library/CloudStorage/OneDrive-UniversityofEasternFinland/Projects/Minna/2_Target_Hits.txt', 'w', 1)
f_m_1.write ("Target_Gene" + "\t" + "Total_Count" + "\n")

for file_names in files:
	c = 0
	path_split = PurePath(file_names).parts
	file_name_gene = path_split [9]
	file_name_gene_DE = file_name_gene.split (".")
	Gene_Name = file_name_gene_DE [0].split ("_")
	with open (file_names, 'r') as myFile:
		line = myFile.readline ()
		for line in myFile:
			line = line.replace (',', '.')
			line_list = line.split ("\t")
			if float(line_list [6]) < 0.05:
				f_m.write (str (Gene_Name [1]) + "\t" + str (line_list [0]) + "\t" + str (line_list [2]) + "\t" + str (line_list [8]) + "\n")
				c = c + 1
	f_m_1.write (str (Gene_Name [1]) + "\t" + str (c) + "\n")
