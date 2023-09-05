def DNA_strand(dna):
    # dna is a string
    dnaOut=""
    ns=""
    
    for symbol in dna:
        if symbol== "A":
            ns="T"
        elif symbol== "T":
            ns="A"
        elif symbol== "C":
            ns="G"
        elif symbol== "G":
            ns="C"
    
        dnaOut=dnaOut + ns
    
    return dnaOut

print(DNA_strand("TAACG"))