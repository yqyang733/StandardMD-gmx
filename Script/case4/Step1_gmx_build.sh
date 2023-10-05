source /public/software/apps/gromacs/2022.2/bin/GMXRC.bash
export LD_LIBRARY_PATH=/public/software/lib/:$LD_LIBRARY_PATH
source /public/software/compiler/intel/intel-compiler-2017.5.239/bin/compilervars.sh intel64

echo 2|gmx pdb2gmx -f PRO.pdb -o build.gro -water tip3p -ignh
gmx editconf -f SOL.pdb -o SOL.gro
python merge_gro.py
python merge_top.py
gmx editconf -f build_1.gro -o newbox.gro -bt cubic -d 0.8
gmx solvate -cp newbox.gro -cs spc216.gro -p topol.top -o solv.gro
gmx grompp -f ions.mdp -c solv.gro -p topol.top -o ions.tpr -maxwarn 2
gmx genion -s ions.tpr -o solv_ions.gro -p topol.top -pname SOD -nname CLA -neutral -conc 0.15
gmx make_ndx -f solv_ions.gro -o index.ndx