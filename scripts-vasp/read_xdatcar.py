# -*- coding: utf-8 -*-
import os
import sys
def read_xdatcar(filename, frame):
    with open(filename, 'r') as xdatcar_file:
        lines = xdatcar_file.readlines()
     
        num_atoms = sum(int(num) for num in lines[6].split())

        num_frames = (len(lines) - 7) // (num_atoms + 1)
        
        if frame >= num_frames or frame < 0:
            raise ValueError(f"Frame number out of range. There are only {num_frames} frames available.")

 
    start_line = frame * (num_atoms + 1) + 8
    end_line = start_line + num_atoms
    

    poscar_filename = f'POSCAR_{frame}'
    

    with open(poscar_filename, 'w') as poscar_file:

        for i in range(7):
            poscar_file.write(lines[i])
        poscar_file.write("Direct\n")

        for i in range(start_line, end_line):
            poscar_file.write(lines[i])
            
    print(f"POSCAR file for frame {frame} has been written to {poscar_filename}.")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python read_xdatcar.py <filename> <frame>")
        sys.exit(1)

    filename = sys.argv[1]
    frame = int(sys.argv[2])

    read_xdatcar(filename,frame)    