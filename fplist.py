def mycalcfp(sp):
        """Calculate a molecular fingerprint.
        
        Optional parameters:
           fptype -- the fingerprint type (default is "FP2"). See the
                     fps variable for a list of of available fingerprint
                     types.
        """
        fp = ob.vectorUnsignedInt()
        try:
            fingerprinter = _fingerprinters["FP3"]
        except KeyError:
            raise ValueError("%s is not a recognised Open Babel Fingerprint type" % fptype)
		for i in sp
		string smartsstring;
    OBSmartsPattern obsmarts;
    string description;
    int numbits;
    int numoccurrences;
    int bitindex;	
        fingerprinter.GetFingerprint(self.OBMol, fp)
        return Fingerprint(fp)
string smartsstring;
    OBSmartsPattern obsmarts;
    string description;
    int numbits;
    int numoccurrences;
    int bitindex;