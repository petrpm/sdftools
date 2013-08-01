import pybel
err=open("e:\\cheminf\\sdf\\rem_err.txt","w")
sdf=pybel.readfile("sdf","e:\\cheminf\\sdf\\order2.sdf")
out=pybel.Outputfile("sdf","e:\\cheminf\\sdf\\order3.sdf",True)
l=0
sr=0
for i in sdf:
    frag=i.OBMol.Separate()
    if len(frag)>1:
        flag=0
        for k in frag:
            fla=k.GetFormula()
            if fla=="ClH" or fla=="HCl":
                flag=flag+1
                i.data['saltdata']="HCl"
            elif fla=="BrH" or fla=="BrH":
                flag=flag+1
                i.data['saltdata']="HBr"
        if flag==len(frag)-1:
            if i.OBMol.StripSalts(2):
                sr=sr+1
                err.write("Salts stripped from id-"+i.data['ID']+"\n")
                out.write(i)
            else: err.write("failed to strip Salts from id-"+i.data['ID']+"\n")
        else: err.write("fragment error at id-"+i.data['ID']+"\n")
    else: out.write(i)                    
    l=l+1
print ("processed-",l,"\nsalt removed from",sr)   
