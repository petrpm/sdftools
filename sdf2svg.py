import pybel
import subprocess
import sys

iter=pybel.readfile("sdf",sys.argv[1])
for mol in iter:
    mol.write("mol","svg/1.mol",overwrite=True)
    #catnum=mol.data["Catalog Number"].replace("PKCBB","PKB").rstrip()
    mol.OBMol.StripSalts()
    catnum=mol.write("inchikey").strip()
    proc=subprocess.call("indigo-depict.exe svg/1.mol"+" svg/"+catnum+".svg -h 200 -w 200")
   