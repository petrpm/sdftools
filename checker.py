import pybel
import sys
import re


err=open("rem_err.txt","w")
sdf=pybel.readfile("sdf",sys.argv[1])
fl=0;
str=""
for i in sdf:
    
    
    if ('Chemical_Name' not in i.data): 
        str+="no Chemical_Name\n"
        fl=1
    if ('Availability' in i.data): 
            if ('salt data' not in i.data): 
                str+="no salt data\n"
                fl=1 
            if ('Price group' not in i.data): 
                str+="no Price group\n"
                fl=1     
    if(fl):
         if ('Catalog Number' not in i.data): print("NO Catalog Number")
         else:
             str=i.data['Catalog Number']+"\n"+str
             print (str)
             str=""
             fl=0;    
    