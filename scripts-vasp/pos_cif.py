import os
from pymatgen.core import Structure

#从pos to cif

# 定义元素集合
metals = {"Ti", "V", "Mn", "Fe", "Co", "Ni", "Zr", "Nb", "Mo", "Rh", "Ru", "Pd"}

slab_path = '/share/home/dinghaowen/aimd/descriptor/slab'

# 遍历元素集合并生成 CIF 文件
for m in metals:
    # 定义元素目录路径
    element_path = os.path.join(slab_path, m)
    
    if os.path.isdir(element_path):
        os.chdir(element_path)  # 切换到元素目录

        # 检查 CONTCAR 文件是否存在
        input_file = "CONTCAR"
        if os.path.exists(input_file):
            # 读取 CONTCAR 文件并生成结构
            structure = Structure.from_file(input_file)
            
            # 定义输出 CIF 文件的路径
            output_file = os.path.join(slab_path, f"CONTCAR_{m}.cif")
            
            # 保存为 CIF 格式
            structure.to(filename=output_file, fmt='cif')
            print(f"Converted {input_file} to {output_file}")
        else:
            print(f"Input file {input_file} not found in {element_path}. Skipping...")
    else:
        print(f"Directory {element_path} does not exist. Skipping...")


#从cif to pos

def convert_cif_to_poscar(cif_file, output_file="POSCAR"):
    # 读取 CIF 文件
    structure = Structure.from_file(cif_file)

    # 写入 POSCAR 格式
    structure.to(fmt="poscar", filename=output_file)
    print(f"Converted {cif_file} to {output_file}")

# 元素集合，使用字符串
metals = {"Ti", "V", "Mn", "Fe", "Co", "Ni", "Zr", "Nb", "Mo", "Rh", "Ru", "Pd"}
path = '/share/home/dinghaowen/aimd/descriptor/slab'

for m in metals:
    # 定义元素目录路径
    element_path = os.path.join(path, m)

    # 检查元素目录是否存在
    if not os.path.isdir(element_path):
        print(f"Directory {element_path} does not exist. Skipping.")
        continue

    # 检查 CIF 文件是否存在于元素目录中
    cif_file = os.path.join(element_path, f"{m}.cif")
    if os.path.exists(cif_file):
        # 切换到元素目录并执行转换
        os.chdir(element_path)
        convert_cif_to_poscar(cif_file)
    else:
        print(f"{cif_file} not found in {element_path}. Skipping.")
