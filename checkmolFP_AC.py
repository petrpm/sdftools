import sys
import pybel
import subprocess
outfile=open("checkmolout.fpt","w")
molfile=pybel.readfile("sdf",sys.argv[1])
#mol=next(molfile)
def makefp(mol):
    tmp=open("tmpmol.mol","w")
    tmp.write(mol.write("mol"))
    tmp.close()
    str=subprocess.Popen(("checkmol.exe","-H","tmpmol.mol"),stdout=subprocess.PIPE,universal_newlines=True)
    return str.stdout.read()
i=0
for mol in molfile:
    i+=1
    print(i)
    outfile.write(mol.write("inchikey").rstrip()+","+mol.data['ID_']+","+makefp(mol).split(";")[0]+"\n")
outfile.close()