import sys
import pybel
infile=pybel.readfile("sdf",sys.argv[1])
molcount=0
inchis=[]
for mol in infile:
    inchi=mol.write("inchi")
    if inchi in inchis:
        molcount+=1
    else:
        inchis.append(inchi)
print("Total records: ",molcount)  
