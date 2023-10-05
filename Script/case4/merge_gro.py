import os
import shutil

class config:

    def __init__(self):

        self.solv = "build.gro"
        self.hoh = "SOL.gro"

def merge(solv, hoh):
    
    with open(solv) as f:
        solv_lines = f.readlines()

    with open(hoh) as f:
        hoh_lines = f.readlines()

    all_atom_num = int(solv_lines[1].strip()) + int(hoh_lines[1].strip())
    rt = open("build_1.gro", "w")
    rt.write("\n "+str(all_atom_num)+"\n" + "".join(solv_lines[2:-1]) + "".join(hoh_lines[2:-1]) + solv_lines[-1])
    rt.close()

    hoh_num = open("hoh_num.dat", "w")
    hoh_num.write(str(int(hoh_lines[1].strip())/3)+"个水分子。")

def run():

    settings = config()
    merge(settings.solv, settings.hoh)                                                                                                                                                         

def main():

    run()
    
if __name__=="__main__":
    main() 