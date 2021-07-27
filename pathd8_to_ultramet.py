# Made by Dennis Larsson @ University of Vienna - 27th July 2021 
#
# Before running this script make sure to give the PATHd8 executable file proper permissions. This is done by typing this into the terminal 
# while the terminal is standing where the executable is located (in my case in the directory "/home/biogeoanalysis/scriptMona/"): chmod +x PATHd8
# To run this script type the following into the terminal while the terminal is standing in the folder which contains 
# this script, the template file, the newick file and the PATHd8 executable file:
# python3 pathd8_to_ultramet.py Iris_rooted.nwk template.tre
# where "Iris_rooted.nwk" is the newick file that contains all the trees that should be converted to ultrametric and "template.tre" is the template 
# for the input file for PATHd8 (which contains the sequence length at the top and the mrca info in the bottom).

import os
import sys

nwk = sys.argv[1]
tmp = sys.argv[2]

templateInfo = []
with open (tmp) as templateFile:
	for line in templateFile:
		templateInfo.append(line)

seqLen = templateInfo[0]
mrca = templateInfo[-1]

newickOutFilename = nwk.split(".")[0] + "_UM.nwk"
i = 1
with open (nwk) as newickFile:
	#line = newickFile.readline()
	newickOut = open (newickOutFilename, "w")
	for line in newickFile:
		print("Processing tree number: " + str(i))
		InputFile = open ("inputfile" + str(i) + ".tre", "w")
		#print((templateInfo[0] + "\n" + line + "\n" + templateInfo[-1]))
		InputFile.write(templateInfo[0] + "\n" + line + "\n" + templateInfo[-1])
		InputFile.close()
		os.system("./PATHd8 inputfile" + str(i) + ".tre " + "outputfile" +  str(i) + ".txt")
		os.remove("inputfile" + str(i) + ".tre")
		
		with open ("outputfile" +  str(i) + ".txt") as P8outputFile:
			for line in P8outputFile:
				if "d8 tree" in line:
					newickOut.write(line.split(" ")[-1])
					break
		os.remove("outputfile" +  str(i) + ".txt")
		i+=1
newickOut.close()
