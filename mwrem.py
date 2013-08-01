import pybel
import sys
err=open("rem_err.txt","w")
sdf=pybel.readfile("sdf",sys.argv[1])
out=pybel.Outputfile("sdf","_out.sdf",True)
l=0
for i in sdf:
    if (i.molwt<450): out.write(i) 
    l=l+1      
print ("processed-",l,"\nsalt removed from",sr)   
                    
        