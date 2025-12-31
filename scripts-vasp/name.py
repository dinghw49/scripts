import os

# 获取当前目录
current_dir = os.getcwd()

# 遍历当前目录下的所有文件夹
for folder_name in os.listdir(current_dir):
    folder_path = os.path.join(current_dir, folder_name)
    if os.path.isdir(folder_path):
        contcar_path = os.path.join(folder_path, "CONTCAR")
        if os.path.isfile(contcar_path):
            # 读取文件内容
            with open(contcar_path, 'r') as f:
                lines = f.readlines()

            if not lines:
                print(f"{contcar_path} 是空文件，已跳过。")
                continue

            # 修改第一行
            lines[0] = f"Ni_Pol_{folder_name}\n"

            # 写回文件
            with open(contcar_path, 'w') as f:
                f.writelines(lines)

            print(f"已修改 {contcar_path} 的第一行为 Ni_Pol_{folder_name}")
        else:
            print(f"{folder_name} 中没有 CONTCAR 文件")
