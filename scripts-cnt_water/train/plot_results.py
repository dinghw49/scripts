import numpy as np
import matplotlib.pyplot as plt

# 如果在服务器/无显示环境，取消下一行注释以避免 plt.show() 报错
# import matplotlib
# matplotlib.use('Agg')

# 读取数据（对应 MATLAB 的 load *.out）
# 假设为空白分隔的纯文本数据，列数与 MATLAB 中一致
energy_train = np.loadtxt('energy_train.out')
force_train = np.loadtxt('force_train.out')

# 全局字体与数学字体设置（不强依赖 LaTeX）
plt.rcParams.update({
    'font.size': 15,
    'mathtext.fontset': 'cm',   # 采用 Computer Modern 风格
    'axes.labelsize': 15,
    'xtick.labelsize': 15,
    'ytick.labelsize': 15,
})

# -----------------------------
# Figure 1: Energy scatter 与 y=x 参考线
fig1, ax1 = plt.subplots()

# 注意：MATLAB 为 1 基索引，Python/NumPy 为 0 基索引
ax1.plot(energy_train[:, 1], energy_train[:, 0], '.', markersize=20)

# 参考线 y = x，采用数据的最小最大值
x_ref = np.linspace(min(energy_train[:, 1].min(), energy_train[:, 0].min())-2,
                    max(energy_train[:, 1].max(), energy_train[:, 0].max())+2, 100)
ax1.plot(x_ref, x_ref, linewidth=2)

# 轴标签（用 mathtext 写物理量单位）
ax1.set_xlabel(r'DFT energy (eV/atom)')
ax1.set_ylabel(r'NEP energy (eV/atom)')

# 刻度线长度（Matplotlib 用像素长度；MATLAB 的 ticklength 是相对比例）
ax1.tick_params(which='major', length=6)  # 主刻度
ax1.tick_params(which='minor', length=3)  # 次刻度（如需）
ax1.minorticks_on()

# axis tight 等价：根据数据自动紧密包裹
ax1.autoscale(enable=True, tight=True)

fig1.tight_layout()

# -----------------------------
# Figure 2: Force scatter（3 分量）与 y=x 参考线
fig2, ax2 = plt.subplots()

# plot force 与三分量
ax2.plot(force_train[:, 3:6], force_train[:, 0:3], '.', markersize=20)

# 参考线 y = x，采用数据的最小最大值
x_ref2 = np.linspace(min(force_train[:, 3:6].min(), force_train[:, 0:3].min()),
                     max(force_train[:, 3:6].max(), force_train[:, 0:3].max()), 100)
ax2.plot(x_ref2, x_ref2, linewidth=2)

# 轴标签（用 mathtext 表示 Å）
ax2.set_xlabel(r'DFT force (eV/$\mathrm{\AA}$)')
ax2.set_ylabel(r'NEP force (eV/$\mathrm{\AA}$)')

ax2.tick_params(which='major', length=6)
ax2.tick_params(which='minor', length=3)
ax2.minorticks_on()

ax2.autoscale(enable=True, tight=True)
fig2.tight_layout()

# -----------------------------
# 保存与显示（可按需修改文件名/格式）
fig1.savefig('energy_scatter.png', dpi=300, bbox_inches='tight')
fig2.savefig('force_scatter.png', dpi=300, bbox_inches='tight')

plt.show()  # 在无图形界面的服务器上可省略，并使用 Agg 后端仅保存