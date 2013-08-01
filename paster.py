import sys
import pybel
outfile=pybel.Outputfile("sdf",sys.argv[1]+".sdf")
molcount=0
files=sys.argv[2:]
for file in files:
    infile=pybel.readfile("sdf",file)
    for mol in infile:
        molcount+=1    
        outfile.write(mol)
        print(molcount)
    infile.close()    
    print("Total records: ",molcount)  
