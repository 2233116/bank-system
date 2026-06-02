import os
import shutil
from datetime import datetime

# 👉 改成你的桌面路径
source_folder = r"C:\Users\14384\Desktop"

# 👉 分类规则
file_types = {
    "图片": [".jpg", ".png", ".jpeg"],
    "文档": [".docx", ".doc", ".pdf", ".txt"],
    "视频": [".mp4", ".mov"],
    "压缩包": [".zip", ".rar"]
}

# 👉 获取文件编号（防重名）
def get_next_number(folder_path, prefix):
    if not os.path.exists(folder_path):
        return 1

    nums = []
    for f in os.listdir(folder_path):
        if f.startswith(prefix):
            try:
                num = int(f.split("_")[-1].split(".")[0])
                nums.append(num)
            except:
                pass

    return max(nums, default=0) + 1


# 👉 开始整理
for filename in os.listdir(source_folder):
    file_path = os.path.join(source_folder, filename)

    # 跳过文件夹
    if os.path.isdir(file_path):
        continue

    # 获取扩展名
    ext = os.path.splitext(filename)[1].lower()

    for folder, extensions in file_types.items():
        if ext in extensions:

            # 👉 获取文件修改时间
            timestamp = os.path.getmtime(file_path)
            date_str = datetime.fromtimestamp(timestamp).strftime("%Y-%m")

            # 👉 目标路径：桌面\图片\2026-05
            target_folder = os.path.join(source_folder, folder, date_str)

            os.makedirs(target_folder, exist_ok=True)

            # 👉 新文件名（自动编号）
            index = get_next_number(target_folder, folder)
            new_name = f"{folder}_{index:03d}{ext}"

            target_path = os.path.join(target_folder, new_name)

            # 👉 防止重名
            while os.path.exists(target_path):
                index += 1
                new_name = f"{folder}_{index:03d}{ext}"
                target_path = os.path.join(target_folder, new_name)

            # 👉 移动文件
            shutil.move(file_path, target_path)

            print(f"移动: {filename} → {folder}/{date_str}/{new_name}")
            break

print("✅ 全部整理完成！")
input("按回车键退出... ")