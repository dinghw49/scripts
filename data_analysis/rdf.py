import MDAnalysis as mda
import os
import numpy as np
from MDAnalysis import Universe
from MDAnalysis.analysis import rdf
import matplotlib.pyplot as plt
from MDAnalysis import transformations

# 加载数据
# path = '/scratch/hwding01/cp2k_pure_water'  # 替换为实际路径
file1 = os.path.join('cp2k-pos-1.xyz')
u = Universe(file1)

# 设置模拟盒的维度
dim = np.array([10, 10, 10, 90, 90, 90])  # 盒子维度
transform = mda.transformations.boxdimensions.set_dimensions(dim)
u.trajectory.add_transformations(transform)

# 初始化 RDF 分析对象和结果
rdf_analysis = None  # 初始化 RDF 分析对象
rdf_values_total = None  # 初始化总 RDF 值
num_frames = 0  # 计数帧数

# 遍历指定范围的帧
for ts in u.trajectory[0:2]:  # 从第 5000 帧开始遍历
    # 打印当前处理的帧数
    print(f"Processing frame {num_frames + 1}...")

    # 在每一帧中选择原子
    selection1 = u.select_atoms('name O')  # 选择 O 原子
    selection2 = u.select_atoms('name H')  # 选择 H 原子
    
    # 创建新的 RDF 分析器
    rdf_analysis = rdf.InterRDF(selection1, selection2)
    
    # 计算 RDF
    rdf_analysis.run()
    
    # 累加该帧计算的 RDF
    if rdf_values_total is None:
        rdf_values_total = rdf_analysis.results.rdf.copy()  # 初始化
    else:
        rdf_values_total += rdf_analysis.results.rdf  # 累加
    
    num_frames += 1  # 增加帧计数

# 计算平均 RDF 并绘制结果
if num_frames > 0:
    average_rdf = rdf_values_total / num_frames
import MDAnalysis as mda
import os
import numpy as np
from MDAnalysis import Universe
from MDAnalysis.analysis import rdf

# 加载数据
file1 = os.path.join('cp2k-pos-1.xyz')
u = Universe(file1)

# 设置模拟盒的维度
dim = np.array([10, 10, 10, 90, 90, 90])  # 盒子维度
transform = mda.transformations.boxdimensions.set_dimensions(dim)
u.trajectory.add_transformations(transform)

# 初始化 RDF 分析对象和结果
rdf_analysis = None  # 初始化 RDF 分析对象
rdf_values_total = None  # 初始化总 RDF 值
num_frames = 0  # 计数帧数

# 遍历指定范围的帧
for ts in u.trajectory[0:10]:  # 从第 0 帧开始遍历
    # 打印当前处理的帧数
    print(f"Processing frame {num_frames + 1}...")

    # 在每一帧中选择原子
    selection1 = u.select_atoms('name O')  # 选择 O 原子
    selection2 = u.select_atoms('name H')  # 选择 H 原子
    
    # 创建新的 RDF 分析器
    rdf_analysis = rdf.InterRDF(selection1, selection2)
    
    # 计算 RDF
    rdf_analysis.run()
    
    # 累加该帧计算的 RDF
    if rdf_values_total is None:
        rdf_values_total = rdf_analysis.results.rdf.copy()  # 初始化
    else:
        rdf_values_total += rdf_analysis.results.rdf  # 累加
    
    num_frames += 1  # 增加帧计数

# 计算平均 RDF 并输出结果
if num_frames > 0:
    average_rdf = rdf_values_total / num_frames

    # 保存 rdf_values_total 到文件
    np.savetxt('rdf_values_total.txt', rdf_values_total)

    # 保存 average_rdf 到文件
    np.savetxt('average_rdf.txt', average_rdf)

    print("RDF values saved to 'rdf_values_total.txt' and 'average_rdf.txt'.")
else:
    print("No frames found in trajectory.")
