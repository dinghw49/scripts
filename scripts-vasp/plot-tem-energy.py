import re

# 定义正则表达式来匹配温度和 E0 信息
temperature_pattern = re.compile(r"T=\s+([\d.]+)")
e0_pattern = re.compile(r"E0=\s+([-\d.E+]+)")

def extract_temperature_e0(oszicar_file):
    temperatures = []
    e0_values = []
    
    with open(oszicar_file, 'r') as file:
        for line in file:
            # 查找温度数据
            temp_match = temperature_pattern.search(line)
            if temp_match:
                temperature = float(temp_match.group(1))
                temperatures.append(temperature)
            
            # 查找 E0 数据
            e0_match = e0_pattern.search(line)
            if e0_match:
                e0_value = float(e0_match.group(1))
                e0_values.append(e0_value)

    return temperatures, e0_values

def save_to_file(temperatures, e0_values, output_file):
    with open(output_file, 'w') as f:
        f.write("Temperature (K)    E0 (eV)\n")
        f.write("----------------------------\n")
        for temp, e0 in zip(temperatures, e0_values):
            f.write(f"{temp:<18} {e0:<18}\n")

# 使用示例
oszicar_file = 'OSZICAR'  # 替换为你的OSZICAR文件路径
temperatures, e0_values = extract_temperature_e0(oszicar_file)

# 将提取的数据保存到 data.txt 文件中
output_file = 'data.txt'
save_to_file(temperatures, e0_values, output_file)

import matplotlib.pyplot as plt

# 从 data.txt 文件中读取温度和 E0 值
def read_data(data_file):
    temperatures = []
    e0_values = []
    
    with open(data_file, 'r') as f:
        lines = f.readlines()[2:]  # 跳过前两行标题
        for line in lines:
            parts = line.split()
            temperatures.append(float(parts[0]))  # 第一列是温度
            e0_values.append(float(parts[1]))     # 第二列是 E0 值

    return temperatures, e0_values

def plot_temperature_and_e0(steps, temperatures, e0_values, output_file):
    # 删除 E0 的第一个值
    steps_e0 = steps[1:]       # 删除第一个步数
    e0_values = e0_values[1:]  # 删除第一个 E0 值

    # 创建两张子图
    fig, axs = plt.subplots(1, 2, figsize=(12, 5))  # 创建一行两列的子图，调整整体大小

    # 设置温度的上下限
    temp_min = min(temperatures)
    temp_max = max(temperatures)
    temp_ylim_min = temp_min - 100
    temp_ylim_max = temp_max + 200

    # 子图1：绘制温度曲线
    axs[0].set_title('Temperature vs Step')
    axs[0].set_xlabel('Step')
    axs[0].set_ylabel('Temperature (K)')
    axs[0].scatter(steps, temperatures, color='red', marker='o', s=1)  # s=20 调小点的大小
    axs[0].set_ylim([temp_ylim_min, temp_ylim_max])

    # 子图2：绘制 E0 能量曲线
    axs[1].set_title('E0 Energy vs Step')
    axs[1].set_xlabel('Step')
    axs[1].set_ylabel('E0 Energy (eV)')
    axs[1].scatter(steps_e0, e0_values, color='blue', marker='x', s=1)  # s=20 调小点的大小

    # 调整子图布局，避免重叠
    plt.tight_layout()

    # 保存图像
    plt.savefig(output_file)
    plt.show()

# 使用示例
data_file = 'data.txt'  # 替换为你的 data.txt 文件路径
temperatures, e0_values = read_data(data_file)

# 生成步数（序数）作为 x 轴
steps = list(range(1, len(temperatures) + 1))

# 绘制温度和 E0 能量的图像
output_file = 'temperature_e0_plot.png'
plot_temperature_and_e0(steps, temperatures, e0_values, output_file)

print(f"图像已保存到 {output_file} 中。")