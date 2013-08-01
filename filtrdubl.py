import sys
import pybel
infile=pybel.readfile("sdf",sys.argv[1])
outfile=pybel.Outputfile("sdf","out_"+sys.argv[1])
molcount=0
inchis=[]
for mol in infile:
    inchi=mol.write("inchi")
    if inchi in inchis:
        molcount+=1
    else:
        inchis.append(inchi)
        outfile.write(mol)
print("Total records: ",molcount)  
