import sys
infile=open(sys.argv[1],"r")
molcount=0
fields={};
for oneline in infile:
    if oneline[:4]==">  <":
        fieldname=oneline[4:oneline.rfind("> (")]
        if fieldname in fields:
            fields[fieldname]+=1
        else:
            fields[fieldname]=1    
    if oneline.strip()=="$$$$": 
        molcount+=1
print("Total records: ",molcount)  
for i in fields:
    print (i," - ",fields[i])