# path8d_to_ultrametric

Made by Dennis Larsson @ University of Vienna - 27th July 2021 

Before running this script make sure to give the PATHd8 executable file proper permissions. This is done by typing this into the terminal 
while the terminal is standing where the executable is located (in my case in the directory "/home/biogeoanalysis/scriptMona/"): chmod +x PATHd8
To run this script type the following into the terminal while the terminal is standing in the folder which contains 
this script, the template file, the newick file and the PATHd8 executable file:
python3 pathd8_to_ultramet.py Iris_rooted.nwk template.tre
where "Iris_rooted.nwk" is the newick file that contains all the trees that should be converted to ultrametric and "template.tre" is the template 
for the input file for PATHd8 (which contains the sequence length at the top and the mrca info in the bottom).
