import os
import shutil
from datetime import datetime
import tkinter as tk
from tkinter import messagebox

# 分类规则
file_types = {
    "图片": [".jpg", ".png", ".jpeg", ".gif"],
    "文档": [".pdf", ".docx", ".txt"],
    "视频": [".mp4", ".avi"],
    "压缩包": [".zip", ".rar"]
}

# 桌面路径
desktop = os.path.join(os.path.expanduser("~"), "Desktop")

# 撤销数据
undo_data = []


# 整理函数
def organize_desktop(selected_type, preview=False):

    moved_count = 0
    preview_count = {}

    # 清空撤销记录
    undo_data.clear()

    # 清空日志框
    log_box.delete(1.0, tk.END)

    for filename in os.listdir(desktop):

        # 防止移动自己
        if filename == os.path.basename(__file__):
            continue

        file_path = os.path.join(desktop, filename)

        if os.path.isfile(file_path):

            ext = os.path.splitext(filename)[1].lower()

            # 日志输出
            log_box.insert(tk.END, f"检测文件: {filename}\n")
            log_box.see(tk.END)

            # 跳过快捷方式
            if ext in [".lnk", ".url"]:

                log_box.insert(tk.END, f"跳过快捷方式: {filename}\n")
                log_box.see(tk.END)

                continue

            match = False

            for folder, exts in file_types.items():

                if selected_type != "全部" and folder != selected_type:
                    continue

                if ext in exts:

                    match = True

                    # 预览统计
                    preview_count[folder] = (
                        preview_count.get(folder, 0) + 1
                    )

                    # 预览模式不移动
                    if preview:
                        break

                    # 日期分类
                    date_str = datetime.fromtimestamp(
                        os.path.getmtime(file_path)
                    ).strftime("%Y-%m")

                    target_folder = os.path.join(
                        desktop,
                        folder,
                        date_str
                    )

                    os.makedirs(target_folder, exist_ok=True)

                    new_path = os.path.join(
                        target_folder,
                        filename
                    )

                    # 防重名
                    count = 1

                    while os.path.exists(new_path):

                        name, ext2 = os.path.splitext(filename)

                        new_name = f"{name}_{count}{ext2}"

                        new_path = os.path.join(
                            target_folder,
                            new_name
                        )

                        count += 1

                    # 记录撤销数据
                    undo_data.append((new_path, file_path))

                    shutil.move(file_path, new_path)

                    moved_count += 1

                    log_box.insert(
                        tk.END,
                        f"已移动: {filename}\n"
                    )

                    log_box.see(tk.END)

                    break

            # 未匹配文件
            if not match:

                preview_count["其它"] = (
                    preview_count.get("其它", 0) + 1
                )

                if preview:
                    continue

                other_folder = os.path.join(
                    desktop,
                    "其它"
                )

                os.makedirs(other_folder, exist_ok=True)

                new_path = os.path.join(
                    other_folder,
                    filename
                )

                # 记录撤销数据
                undo_data.append((new_path, file_path))

                shutil.move(file_path, new_path)

                moved_count += 1

                log_box.insert(
                    tk.END,
                    f"移动到其它: {filename}\n"
                )

                log_box.see(tk.END)

    # 预览模式
    if preview:

        message = "预览结果：\n\n"

        for k, v in preview_count.items():
            message += f"{k}: {v} 个\n"

        messagebox.showinfo("预览", message)

    else:

        # 保存撤销记录
        with open("undo_log.txt", "w", encoding="utf-8") as f:

            for old_path, new_path in undo_data:
                f.write(f"{old_path}|{new_path}\n")

        messagebox.showinfo(
            "完成",
            f"整理完成！共移动 {moved_count} 个文件"
        )

        # 启用撤销按钮
        undo_button.config(state="normal")


# 开始整理
def start_sort():

    confirm = messagebox.askyesno(
        "确认",
        "确定开始整理桌面文件吗？"
    )

    if confirm:

        selected = var.get()

        organize_desktop(
            selected_type=selected,
            preview=False
        )


# 预览整理
def preview_sort():

    selected = var.get()

    organize_desktop(
        selected_type=selected,
        preview=True
    )


# 撤销整理
def undo_sort():

    if not os.path.exists("undo_log.txt"):

        messagebox.showwarning(
            "提示",
            "没有可撤销的记录"
        )

        return

    with open("undo_log.txt", "r", encoding="utf-8") as f:

        lines = f.readlines()

    for line in reversed(lines):

        old_path, new_path = line.strip().split("|")

        if os.path.exists(old_path):

            os.makedirs(
                os.path.dirname(new_path),
                exist_ok=True
            )

            shutil.move(old_path, new_path)

    messagebox.showinfo(
        "完成",
        "已撤销整理"
    )

    undo_button.config(state="disabled")


# ===== GUI =====

root = tk.Tk()

root.title("桌面整理工具 Pro")

root.geometry("380x500")

# 标题
tk.Label(
    root,
    text="一键整理桌面文件",
    font=("Arial", 16)
).pack(pady=15)

# 下拉选择
var = tk.StringVar(value="全部")

options = ["全部", "图片", "文档", "视频", "压缩包"]

dropdown = tk.OptionMenu(
    root,
    var,
    *options
)

dropdown.pack(pady=10)

# 预览区域
preview_frame = tk.Frame(root)
preview_frame.pack(pady=5)

tk.Button(
    preview_frame,
    text="预览整理结果",
    font=("Arial", 12),
    command=preview_sort
).pack()

# 整理区域
real_frame = tk.Frame(root)
real_frame.pack(pady=5)

tk.Button(
    real_frame,
    text="开始整理",
    font=("Arial", 12),
    command=start_sort
).pack()

# 撤销按钮
undo_button = tk.Button(
    real_frame,
    text="撤销整理",
    font=("Arial", 12),
    command=undo_sort,
    state="disabled"
)

undo_button.pack(pady=5)

# 日志框
log_frame= tk.Frame(root)
log_frame.pack(pady=10, fill=tk.BOTH, expand=True)
scrollbar = tk.Scrollbar(log_frame)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
log_box = tk.Text(
    log_frame,
    height=12,
    width=42
)

log_box.pack(side=tk.LEFT,expand=True, fill=tk.BOTH)

# 退出按钮
tk.Button(
    root,
    text="退出",
    command=root.quit
).pack(pady=10)

root.mainloop()