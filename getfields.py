import pybel
import sys

infile=sys.argv[1]
molfile=pybel.readfile("sdf",infile)
fields=[]
for mol in molfile:
	for field in mol.data:
		if (field not in fields):
			fields.append(field)
for i in fields:
	print(i)
		