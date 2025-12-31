#!/bin/bash

# 遍历所有以 POSCAR_ 开头的文件
for file in POSCAR_*; do
  # 提取文件名后面的数字
  folder_name=${file##*_}
  
  # 创建文件夹（如果不存在）
  mkdir -p "$folder_name"
  
  # 移动文件到对应文件夹
  mv "$file" "$folder_name"
done
