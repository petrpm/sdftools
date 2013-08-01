import pybel
import subprocess
import sys
i=0
iter=pybel.readfile("sdf",sys.argv[1])
for mol in iter:
    print(i)
    i=i+1
    #catnum=mol.data["Catalog Number"].replace("PKCBB","PKB").rstrip()
    mol.OBMol.StripSalts()
    mol.write("mol","png/1.mol",overwrite=True)
    catnum=mol.write("inchikey").strip()
    proc=subprocess.call("indigo-depict.exe png/1.mol"+" png/"+catnum+".png -h 250 -w 250")
   