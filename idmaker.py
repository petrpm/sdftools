import pybel
import sys
err=open("rem_err.txt","w")
sdf=pybel.readfile("sdf",sys.argv[1])
out=pybel.Outputfile("sdf","1_out.sdf",True)
ids=[]
for i in sdf:
    if 'Catalog Number' in i.data:
        num=int(i.data['Catalog Number'][6:])
        if (num in ids):
            err.write("\ndouble id - "+i.data['Catalog Number'])
            del i.data['Catalog Number']
        else: ids.append(num)
    out.write(i);
ids.sort()
max=ids[len(ids)-1]
sdf=pybel.readfile("sdf","1_out.sdf")
out=pybel.Outputfile("sdf","2_out.sdf",True)
for i in sdf:
    if 'Catalog Number' not in i.data:
        max=max+1
        i.data['Catalog Number']="PKCBB_0"+str(max)
    out.write(i)