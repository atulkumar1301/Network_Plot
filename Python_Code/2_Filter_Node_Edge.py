f_m = open ('/Users/akumar/Library/CloudStorage/OneDrive-UniversityofEasternFinland/Projects/Minna/3_Filtered_Node_Edge.txt', 'w', 1)
f_m.write ("Target_Gene" + "\t" + "DE_Gene" + "\n")

l = []
with open ("/Users/akumar/Library/CloudStorage/OneDrive-UniversityofEasternFinland/Projects/Minna/2_Target_Hits.txt", 'r') as myFile:
	line = myFile.readline ()
	for line in myFile:
		line_list = line.split ("\t")
		if int(line_list [1]) < 2:
			l.append (line_list [0])
with open ("/Users/akumar/Library/CloudStorage/OneDrive-UniversityofEasternFinland/Projects/Minna/1_Node_Edge.txt", 'r') as myFile_1:
	line_1 = myFile_1.readline ()
	for line_1 in myFile_1:
		line_list_1 = line_1.split ("\t")
		if line_list_1 [0] not in l:
			f_m.write (line_1)
