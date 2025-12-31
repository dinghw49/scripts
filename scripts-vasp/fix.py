import os

def is_float(value):
    try:
        float(value)
        return True
    except:
        return False

def format_coords_line(parts, flags):
    # 保持对齐格式，使用 10 个字符宽度 + 5 位小数（可根据需要微调）
    return "{:>24.16f}{:>24.16f}{:>24.16f}   {}\n".format(float(parts[0]), float(parts[1]), float(parts[2]), flags)

current_dir = os.getcwd()

for folder_name in os.listdir(current_dir):
    folder_path = os.path.join(current_dir, folder_name)
    if os.path.isdir(folder_path):
        contcar_path = os.path.join(folder_path, "CONTCAR")
        if os.path.isfile(contcar_path):
            with open(contcar_path, 'r') as f:
                lines = f.readlines()

            try:
                direct_index = next(i for i, line in enumerate(lines) if line.strip().lower() == "direct")

                # 如果没有Selective dynamics，插入一行
                if lines[direct_index - 1].strip().lower() != "selective dynamics":
                    lines.insert(direct_index, "Selective dynamics\n")
                    direct_index += 1

                # 修改坐标行
                for i in range(direct_index + 1, len(lines)):
                    parts = lines[i].split()
                    if len(parts) >= 3 and all(is_float(p) for p in parts[:3]):
                        z = float(parts[2])
                        flags = "F F F" if z < 0.20 else "T T T"
                        lines[i] = format_coords_line(parts, flags)
                    else:
                        break  # 不是坐标行就停

                with open(contcar_path, 'w') as f:
                    f.writelines(lines)

                print(f"{folder_name} 中的 CONTCAR 已格式化并标记完成")
            except StopIteration:
                print(f"{folder_name} 中未找到 'Direct' 行，跳过")
        else:
            print(f"{folder_name} 中没有 CONTCAR 文件")

