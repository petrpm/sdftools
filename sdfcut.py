import pybel
import subprocess
import sys
start=int(sys.argv[2])
finish=int(sys.argv[3])
iter=pybel.readfile("sdf",sys.argv[1])
outfile=pybel.Outputfile("sdf","out.sdf",True)
i=0
for mol in iter:
    i+=1
    if (i>=start and i<=finish):
        outfile.write(mol)	
	
   