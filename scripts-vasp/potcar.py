import os
import shutil
from pymatgen.core import Structure

# 定义金属集合和对应的 POTCAR 目录
metals = {"Ti", "V", "Mn", "Fe", "Co", "Ni", "Zr", "Nb", "Mo", "Rh", "Ru", "Pd"}
pot = {
    "Ti": "Ti_sv", 
    "V": "V_sv", 
    "Mn": "Mn_pv", 
    "Fe": "Fe", 
    "Co": "Co", 
    "Ni": "Ni", 
    "Zr": "Zr_sv", 
    "Nb": "Zr_sv",  # 注意：Nb 和 Zr_sv 是一样的
    "Mo": "Mo_sv", 
    "Rh": "Rh_pv", 
    "Ru": "Ru_pv", 
    "Pd": "Pd"
}
path_pot = '/share/home/dinghaowen/POTCAR/PBE'


##这个能够自动生成
def process_poscar_and_potcar(element_path):
    from collections import OrderedDict

    poscar_file = os.path.join(element_path, "POSCAR")
    
    if os.path.exists(poscar_file):
        structure = Structure.from_file(poscar_file)
        element_list = [str(specie) for specie in structure.species]
        unique_elements = OrderedDict.fromkeys(element_list)


        potcar_files = []

        for element in unique_elements:
            potcar_output_path = os.path.join(element_path, f"POTCAR_{element}")
            if element in pot:
                potcar_dir = os.path.join(path_pot, pot[element])
                potcar_file = os.path.join(potcar_dir, "POTCAR")
                if os.path.exists(potcar_file):
                    shutil.copy(potcar_file, potcar_output_path)

                    potcar_files.append(potcar_output_path)
                else:
                    print(f"POTCAR for {element} not found in {potcar_dir}.")
            else:
                potcar_dir = os.path.join(path_pot, element)
                potcar_file = os.path.join(potcar_dir, "POTCAR")
                if os.path.exists(potcar_file):
                    shutil.copy(potcar_file, potcar_output_path)
                    potcar_files.append(potcar_output_path)
                  
                else:
                    print(f"POTCAR for {element} not found in {potcar_dir}.")

        # 创建合并后的 POTCAR 文件
        final_potcar_path = os.path.join(element_path, "POTCAR")
        with open(final_potcar_path, 'w') as final_potcar:
            for potcar_file in potcar_files:
                with open(potcar_file, 'r') as temp_file:
                    final_potcar.write(temp_file.read())
        
        print(f"Merged POTCAR files into {final_potcar_path}")

        # 删除临时 POTCAR 文件
        for potcar_file in potcar_files:
            os.remove(potcar_file)
