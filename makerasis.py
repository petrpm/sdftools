import sys
import pybel
infile=pybel.readfile("sdf",sys.argv[1])
outfile=pybel.Outputfile("sdf","out_"+sys.argv[1])
molcount=0
inchis=[]
for mol in infile:   
    #name="Unknown"
    #if "ID_" in mol.data:
    #    name=mol.data["ID_"].strip()
    if "ID_" in mol.data:
        catnum=mol.data["ID_"].strip()   
        mol.data.clear()
        mol.data["Catalog_number"]=catnum        
        molcount+=1    
        outfile.write(mol)
print("Total records: ",molcount)  
