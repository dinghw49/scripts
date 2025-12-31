for i in */; do
  # 去掉末尾的斜杠，并检查文件夹名是否为数字
  folder_name=${i%/}
  if [[ $folder_name =~ ^[0-9]+$ ]]; then
    # 计算新的文件夹名，将数字加上3000
    new_name=$(( folder_name + 3000 ))
    # 重命名文件夹
    mv "$i" "$new_name/"
  else
    echo "跳过非数字文件夹: $i"
  fi
done
