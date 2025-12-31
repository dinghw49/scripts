for i in *;do cd $i;mv POSCAR_new POSCAR;rm POTCAR;vaspkit -task 103;cd ..;done
