import matplotlib.pyplot as plt
import numpy as np
import matplotlib.font_manager
from scipy.interpolate import UnivariateSpline

# 设置字体为 Arial
arial = matplotlib.font_manager.FontProperties(fname='/share/home/dinghaowen/.local/share/fonts/arial.ttf')
plt.rcParams['font.family'] = 'arial'
plt.rcParams['font.weight'] = 'normal'

input_file = 'grad.dat'

# Open the input file for reading
with open(input_file, 'r') as f:
    r = []
    g = []

    # Read data from the file
    for line in f.readlines():
        line = line.split()
        # Process each line and append data to lists
        if len(line) == 2:
            r.append(float(line[0]))
            g.append(float(line[1]))

# Calculate and print the free energy values
tg = 0.0
with open('free_energy.dat', 'w') as output_file:
    output_file.write(f"{r[0]} {tg}\n")
    for i in range(1, len(r)):
        gg = 0.5 * (r[i] - r[i-1]) * (g[i] + g[i-1])
        tg += gg
        output_file.write(f"{r[i]} {tg}\n")

# 读取数据文件
data = np.loadtxt('free_energy.dat')

# 提取列
r, tg = data[:, 0], data[:, 1]

# 将 tg 的最小值设置为0
tg_min = np.min(tg)
tg -= tg_min



plt.figure(figsize=(8, 6))

# 绘制平滑数据
plt.plot(r, tg, label='Free Energy')

# 标出 y 轴最高点
max_y = np.max(tg)
max_x = r[np.argmax(tg)]

# 添加水平虚线作为参考线
plt.axhline(y=max_y, color='r', linestyle='--', label=f'Max Energy: {max_y:.2f} eV')

# 在最高点位置添加标注
plt.text(max_x, max_y, f'{max_y:.2f} eV', fontsize=15, verticalalignment='bottom', horizontalalignment='right', color='r')

# 设置坐标轴标签和图例
plt.xlabel('Collective variable (Ang)', fontsize=20)
plt.ylabel('Free energy (eV)', fontsize=20)
plt.legend(fontsize=20)
plt.xticks(fontsize=20)
plt.yticks(fontsize=20)
plt.grid(True)

# 保存图片
plt.savefig('free_energy.jpg')

# 显示图片
plt.show()
