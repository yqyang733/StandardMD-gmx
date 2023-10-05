import os
import shutil

class config:

    def __init__(self):

        self.top = "topol.top"
        self.wat_num = str(300)

def gene_hoh_itp():

    hoh_itp = open("HOH.itp", "w")
    hoh_itp.write(
'''[ moleculetype ]
; name  nrexcl
HOH         2

[ atoms ]
; nr    type    resnr   residu  atom    cgnr    charge  mass
     1         OT      1     HOH      O       1    -0.834000    15.9994   ; qtot -0.834
     2         HT      1     HOH     H01      2     0.417000     1.0080   ; qtot -0.417
     3         HT      1     HOH     H02      3     0.417000     1.0080   ; qtot  0.000

;[ settles ]
; OW    funct   doh     dhh
;    1     1  9.572000e-02  1.513900e-01

[ constraints ]
; ai aj funct length_A length_B
1   2   1   0.09572
1   3   1   0.09572
2   3   1   0.15139

[ exclusions ]
    1     2     3
    2     1     3
    3     1     2

#ifdef POSRES_HOH
; Position restraint for each water oxygen
[ position_restraints ]
;  i funct       fcx        fcy        fcz
   1    1       1000       1000       1000
#endif
'''
    )

def merge(top, wat):
    
    with open(top) as f:
        topol = f.readlines()

    rt = open("topol.toptmp", "w")
    for i in topol:
        if i == "; Include water topology\n":
            rt.write("#include \"HOH.itp\"\n\n"+i)
        else:
            rt.write(i)
    rt.write("HOH                   " + wat + "\n")

    os.rename("topol.top", "topol_1.top")
    os.rename("topol.toptmp", "topol.top")  

def run():

    settings = config()
    gene_hoh_itp()
    merge(settings.top, settings.wat_num)                                                                                                                                                         

def main():

    run()
    
if __name__=="__main__":
    main() 