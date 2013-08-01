import pybel
import sys
import re

err=open("rem_err.txt","w")
sdf=pybel.readfile("sdf",sys.argv[1])
fl=0;
i=0;
str=""
print("report:\n")
for mol in sdf:
    i+=1
    if(len(mol.OBMol.Separate())>1):
        print("fragments in - ",mol.data['Catalog Number'],"\n")
    if ('Availability' in mol.data):
        if('Price group' not in mol.data):
            print("no pricegroup in -",mol.data['Catalog Number'],"\n")
print("processed ",i, "molecules")
        
        