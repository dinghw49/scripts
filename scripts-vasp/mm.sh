for  i in *; do cd $i; mv * POSCAR;cp ~/aimd/adsorb/INCAR .; cp ~/aimd/adsorb/KPOINTS .;vaspkit -task 103; cd ..; done
