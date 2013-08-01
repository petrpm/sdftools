import sys
import pybel
infile=pybel.readfile("sdf",sys.argv[1])
outfile=pybel.Outputfile("sdf","out_"+sys.argv[1])
molcount=0
inchis=[]
for mol in infile:
    if "MOL_ID" in mol.data:
        catnum="ASCL-"+"{0:06d}".format(int(mol.data["MOL_ID"].strip()))
        mol.data.clear()
        mol.data["Catalog_number"]=catnum
        molcount+=1    
        outfile.write(mol)
print("Total records: ",molcount)  
