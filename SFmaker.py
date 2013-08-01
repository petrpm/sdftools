import pybel
import sys
import re
regex=re.compile("(^\d+[,|.]?\d*)g?")
w=(1,5,10,25,50,100)
pr=([20,58,98,195,337,594],[40,122,204,400,693,1220],[75,260,430,776,1289,2293],[140,464,784,1556,2544,4292],[270,967,1739,3334,5337,10009],[380,1305,2229,4446,8145,14560],[495,1723,2945,5859,10771,19267])
prmg=(10,20,36,59,114,162,211)

err=open("rem_err.txt","w")
sdf=pybel.readfile("sdf",sys.argv[1])
out=pybel.Outputfile("sdf","SF_out.sdf",True)
ids=[]
for i in sdf:
    #print(i.data['Catalog Number'],"\n")
    mol=pybel.readstring("mol",i.write("mol"))
    mol.data['Catalog Number']=i.data['Catalog Number'] 
    #print(mol.data['Catalog Number'],"\n")
    mol.data['Chemical_Name']=i.data['Chemical_Name']
    if ('salt data' in i.data): mol.data['salt data']=i.data['salt data']
    else: mol.data['salt data']="none"
    if ('Purity' in i.data): mol.data['Purity']=i.data['Purity']
    else: mol.data['Purity']="95%"
    mol.data['EXP_Property']='Available'
    mol.data['delivery time']='2 weeks'
    mol.data["Availability "]="in stock"
    if ('CAS Number' in i.data): mol.data['CAS Number']=i.data['CAS Number']
    if ('Availability' in i.data):
        av=regex.findall(i.data['Availability'])[0]
        av=av.replace(",",".")
        av=float(av)
        if ('Price group' in i.data):
            prg=int(i.data['Price group'])
            if ((av< 1) & (av>=0.1)):
                 mol.data["Quantity 1"]="0.1"
                 mol.data["Unit 1"]="g"
                 mol.data["Price 1"]='$ '+str(prmg[prg-1])
                 #mol.data["Currency 1"]="USD"
                 
            else: 
                 for k in range(6):
                     z=k+1;
                     if (av>=w[k]):
                         mol.data["Quantity "+str(z)]=str(w[k])
                         mol.data["Unit "+str(z)]="g"
                         mol.data["Price "+str(z)]='$ '+str(pr[prg-1][k])
                         #mol.data["Currency "+str(z)]="USD"
                         
        else:   print(mol.data['Catalog Number'],"\n")
        mol.data['Link']="pkchem.ru/compound.php?id="+mol.data['Catalog Number']
        #mol.data['Price group']=i.data['Price group']
        out.write(mol);           
                 
            
    
