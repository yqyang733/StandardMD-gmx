# StandardMD-gmx
Scripts for Standard MD with Gromacs    

## Case1  
Descriptions:   
 - System: Only protein; Only one file      
 - Forcefield: Charmm  
 - Modelling methods: pdb2gmx  

Path:  
 - [Case1](./Script/case1/)  

Usage:  
 - python Step1_generate_gro_top_command.py input.pdb  
 - python Step2_generate_mdp.py  
 - python Step3_generate_submit_sh.py  

## Case2  
Descriptions: 
 - System: Only protein; Multi files   
 - Forcefield: Charmm   
 - Modelling methods: pdb2gmx      

Path:   
 - [Case2](./Script/case2/)  

Usage:  
 - sh Step4_Multitask.sh  