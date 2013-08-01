import pybel
import sys
import re
#err=open("rem_err.txt","w")

class Sdffile:# implement + - XOR and
    def __init__(self):
        self.mols=[]
        self.index=0
        self.stopindex=0
        
    def __iter__(self):
        self.stopindex=len(self.mols)
        return self
    
    def __next__(self):
        if (self.index<self.stopindex):
            mol=self.mols[self.index]
            self.index+=1
            return mol
        else:
            self.index=0;
            raise StopIteration
    
    def readsdf(self,filename):
        molfile=pybel.readfile("sdf",filename)
        self.mols[:] = []
        for i in molfile:
            self.mols.append(i)
        return self.mols
        
    def calcfp(self,fpobject): # возможность вывода описания
        tmp = []
        for mol in mols:            
            tmp.append(fpobject.calcfp(mol))
        return tmp
        
class Fingerprint:
    def __init__(self,fgprint):
        self.fgprnt=fgprint
        self.index=0
        self.numofbits=len(fgprint)
        
    def splitfpdec(self,wordsize,numofwords): #ret list of splited fp портит исходный массив
        tmp=[]
        for i in range(wordsize*numofwords-self.numofbits):
            self.fgprnt.append(0) #add zeroes
        for k in range(numofwords):
            word=self.fgprnt[k*wordsize:(k+1)*wordsize-1]
            fpt=0
            for j in range(len(word)):
                if word[j]==1:
                    fpt=fpt|(2**j)
            tmp.append(fpt)
        return tmp
        
    def printfp(self,wordsize,numofwords,sep='\t', end='\n', filename=sys.stdout):
        splitedfp=self.splitfpdec(wordsize,numofwords)
        tmp=""
        for i in splitedfp:
            tmp=tmp+str(i)+sep
        tmp=tmp[0:-1]
        print (tmp,end=end,file=filename)   

        
class FpCalc:
    def __init__(self,filename="patterns.txt",wordsize=32,numofwords=2):
        self.fgprnt=[]
        self.index=0
        self.readpatterns(filename)
        self.wordsize=wordsize
        self.numofwords=numofwords
        
    def readpatterns(self,filename):
        infile=open(filename,"r")
        self.patterns=[]
        k=0
        for i in infile:
            k=k+1
            tmp=i.split(":")
            try:
                self.patterns.append(pybel.Smarts(tmp[1].strip()))
            except IOError: 
                print("invalid smarts in line-",k,"\n")
                self.patterns.append(pybel.Smarts("[Ir][Ra][Ti][O][N][Al]"))    #imposible to encounter smarts   
        self.numofbits=k 
        return k
        
    def calcfp(self,mol): # возможность вывода описания
        fgprnt=[]      
        for smarts in self.patterns:
            bit=0
            if(smarts.findall(mol)!=[]):
                bit=1
            fgprnt.append(bit)    
        return Fingerprint(fgprnt)
    
    
        
    
     
#add more friendly way to extract moldata  
     
def Field(self,fieldname,fail="unknown"):
    if(fieldname not in self.data):
        return fail
    return self.data[fieldname]
    
    
pybel.Molecule.field=Field
#
fpg=FpCalc("./fplists/groups_fp.fp")#3
fpr=FpCalc("./fplists/cycles_fp.fp")#2
fpm=FpCalc("./fplists/misc_fp.fp")#1
mols=Sdffile()
mols.readsdf(sys.argv[1])
#import subprocess
#proc=subprocess.Popen("indigo-depict "+sys.argv[1]+" svg/_%s.svg -h 200 -w 200")
fpgs=mols.calcfp(fpg)#3
print("-------",len(fpgs))
fprs=mols.calcfp(fpr)#2
print("-------",len(fpgs))
fpms=mols.calcfp(fpm)#1
print("-------",len(fpgs))

outfile=open("fingerprints.txt","w")
for fprt in range(len(fpgs)):
    fpgs[fprt].printfp(32,3,sep='\t', end='\t', filename=outfile)
    fprs[fprt].printfp(32,2,sep='\t', end='\t', filename=outfile)
    fpms[fprt].printfp(32,1,sep='\t', end='\n', filename=outfile)
outfile.close()

outfile=open("moldata.txt","w")
for mol in mols:
    #mol_id - AI	
    catalog_num = mol.field("ID_") 
    chem_name = mol.field("Text_") 
    cas = mol.field("CAS#") 
    #salt = mol.field("salt data") 
    purirty = "95"	
    #logp = mol.field("LogP")	
    avail = "10000"#mol.field("Availability") 	
    #pricegroup = mol.field("Price group") 	
    formula=mol.formula 	
    mo_lweight = str(mol.molwt) 	
    struct=mol.write("mol") 
    strng=catalog_num+"\t"+chem_name+"\t"+cas+"\t""""+salt+"\t"""+purirty+"\t""""+logp+"\t"""+avail+"\t""""+pricegroup+"\t"""+formula+"\t"+mo_lweight+"\t"+struct+"$$$$"
    outfile.write(strng)
outfile.close()    
#import MySQLdb
#import MySQLdb.cursors
#db = MySQLdb.connect(host="localhost", user="root", passwd="", db="tmp")
#cur = db.cursor()
#db.set_character_set('latin1')
#cur.execute('SET NAMES utf8;')
#cur.execute("SELECT * FROM nmr3 ;")
#row = cur.fetchall()

#LOAD DATA INFILE 'e:/cheminf/sdf/sdf_tools/moldata.txt' INTO TABLE `properties` LINES TERMINATED BY '$$$$' (`catalog_num`,`chem_name`,`cas`,`salt`,`purirty`,`logp`,`avail`,`pricegroup`,`formula`,`mo_lweight`,`struct`)
#LOAD DATA INFILE 'e:/cheminf/sdf/sdf_tools/fingerprints.txt' INTO TABLE `fpt` (fpg1,fpg2,fpg3,fpr1,fpr2,fpm)
