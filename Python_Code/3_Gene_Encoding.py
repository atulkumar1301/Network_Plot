f_m = open ('/Users/akumar/Library/CloudStorage/OneDrive-UniversityofEasternFinland/Projects/Minna/5_a_Filtered_Node_Edge_Positive.txt', 'w', 1)
f_m.write ("Target_Gene_coded" + "\t" + "DE_Gene_coded" + "\t" + "Target_Gene" + "\t" + "DE_Gene" + "\t" + "RNA_Log2FC" + "\t" + "PRTB_Log2FC" + "\n")

f_m_1 = open ('/Users/akumar/Library/CloudStorage/OneDrive-UniversityofEasternFinland/Projects/Minna/5_b_Filtered_Node_Edge_Negative.txt', 'w', 1)
f_m_1.write ("Target_Gene_coded" + "\t" + "DE_Gene_coded" + "\t" + "Target_Gene" + "\t" + "DE_Gene" + "\t" + "RNA_Log2FC" + "\t" + "PRTB_Log2FC" + "\n")

with open ("/Users/akumar/Library/CloudStorage/OneDrive-UniversityofEasternFinland/Projects/Minna/3_Filtered_Node_Edge.txt", 'r') as myFile:
	line = myFile.readline ()
	for line in myFile:
		line_list = line.split ("\t")
		DE_Gene = line_list [1].strip ('\"')
		with open ("/Users/akumar/Library/CloudStorage/OneDrive-UniversityofEasternFinland/Projects/Minna/4_Gene_Symbol_Coding.txt", 'r') as myFile_1:
			line_1 = myFile_1.readline ()
			for line_1 in myFile_1:
				line_list_1 = line_1.split ("\t")
				if line_list [0] == line_list_1 [0]:
					Target_Gene_coded = line_list_1 [1]
				if DE_Gene == line_list_1 [0]:
					DE_Gene_coded = line_list_1 [1]
			if float(line_list [2]) > 0 :
				f_m.write ((str (Target_Gene_coded).rstrip()) + "\t" + (str (DE_Gene_coded).rstrip()) + "\t" + (line))
			elif float(line_list [2]) < 0 :
				f_m_1.write ((str (Target_Gene_coded).rstrip()) + "\t" + (str (DE_Gene_coded).rstrip()) + "\t" + (line))
