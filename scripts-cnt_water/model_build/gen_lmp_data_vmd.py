#!/usr/bin/python3
# -*- coding: UTF-8 -*-
"""
@Description :   
@Author      :   KiwiWan 
@Email       :   wankaiweii@gmail.com
@Version     :   v1.0
@Time        :   2022/08/01 12:32:21
"""

def gen_lmp_data(pdb_file):
    import os
    pdb_name = '.'.join(pdb_file.split('.')[:-1])
    tcl_cmd = '''package require topotools;
topo clearbonds;

set sel_H [atomselect top "element H"];
$sel_H set charge 0.5242;
set sel_O [atomselect top "element O"];
$sel_O set charge -1.0484;
set sel [atomselect top "element O H"];

set ids [$sel get index];
foreach {id1 id2 id3} $ids {topo addbond $id1 $id2; topo addbond $id1 $id3; topo addangle $id2 $id1 $id3;}

topo retypebonds;
topo retypeangles;
topo retypedihedrals;
topo retypeimpropers;

mol reanalyze 0;
topo writelammpsdata %s-lmp.data;
quit;    
''' % pdb_name    
    
    ret = os.popen(f"echo '{tcl_cmd}' | vmd -dispdev none {pdb_file}").read()
    #print (tcl_cmd, ret) ##for debug
    return None

if __name__ == '__main__':
    import sys
    pdb_file = sys.argv[1]
    gen_lmp_data(pdb_file)
