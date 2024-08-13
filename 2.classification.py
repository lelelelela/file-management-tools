"""
第一版 根据一个关键字移动文件 

第二版 根据一个关键字移动7个路径下的文件

第三版 根据一个关键字，移动路径下的文件，可以把移动前路径里面所有的文件名包括关键字的文件（包括子文件夹）都移动到移动后路径的里
 
第四版 根据一个关键字，移动路径下的文件，可以把移动前路径里面所有的文件名包括关键字的文件（包括子文件夹）都移动到移动后路径的里。
      输入多个关键词，用回车分隔，随后逐个关键词移动。
"""


import os
import shutil
import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox


def move_files_by_keywords():
    # 获取输入框中的路径和关键字
    path_before = entry_path_before.get()
    path_after = entry_path_after.get()
    keywords = entry_keyword.get("1.0", tk.END).strip().split("\n")

    # 判断目标路径是否存在，不存在则创建
    if not os.path.exists(path_after):
        try:
            os.makedirs(path_after)
        except Exception as e:
            print(f"创建目标路径时出错: {e}")
            return

    # 定义移动文件的函数
    def move_file():
        nonlocal index  # 使用nonlocal关键词来声明index变量为上一层函数move_files_by_keywords中的局部变量
        keyword = keywords[index].strip()

        # 遍历指定路径下的所有文件和文件夹
        for root, dirs, files in os.walk(path_before):
            for file in files:
                if keyword and keyword in file:
                    # 构建源文件路径和目标文件路径
                    source_path = os.path.join(root, file)
                    target_dir = os.path.join(path_after, os.path.relpath(root, path_before))
                    target_path = os.path.join(target_dir, file)

                    # 创建目标文件夹
                    if not os.path.exists(target_dir):
                        try:
                            os.makedirs(target_dir)
                        except Exception as e:
                            print(f"创建目标文件夹时出错: {e}")
                            continue

                    # 移动文件
                    try:
                        shutil.move(source_path, target_path)
                        print(f"成功移动文件: {file}")
                    except Exception as e:
                        print(f"移动文件时出错: {e}")

        index += 1

        if index < len(keywords):
            # 继续移动下一个关键字
            if messagebox.askyesno("提示", f"搞定啦，名字包含\"{keyword}\"的文件都移动过去啦，是否继续移动下一个关键词？"):
                move_file()
            else:
                messagebox.showinfo("提示", "到此为止，不移动下一个")
        else:
            # 所有文件移动完毕
            messagebox.showinfo("提示", f"名字包含\"{keyword}\"的文件已移动过去\n所有文件名包含你给出的关键字的文件均已移动完毕")

    index = 0
    move_file()


def browse_button_path_before():
    # 弹出文件选择对话框，选择移动前的路径
    selected_path = filedialog.askdirectory()
    entry_path_before.delete(0, tk.END)
    entry_path_before.insert(tk.END, selected_path)


def browse_button_path_after():
    # 弹出文件选择对话框，选择移动后的路径
    selected_path = filedialog.askdirectory()
    entry_path_after.delete(0, tk.END)
    entry_path_after.insert(tk.END, selected_path)


# 创建主窗口
window = tk.Tk()
window.title("文件移动")

# 创建移动前路径输入框和浏览按钮
frame_path_before = tk.Frame(window, padx=20)
frame_path_before.grid(row=0, column=0, sticky="w")

label_path_before = tk.Label(frame_path_before, text="移动前路径:")
label_path_before.pack(side=tk.LEFT)

entry_path_before = tk.Entry(frame_path_before, width=40)
entry_path_before.pack(side=tk.LEFT)

button_browse_before = tk.Button(frame_path_before, text="浏览", command=browse_button_path_before)
button_browse_before.pack(side=tk.LEFT)

# 创建移动后路径输入框和浏览按钮
frame_path_after = tk.Frame(window, padx=20)
frame_path_after.grid(row=1, column=0, sticky="w")

label_path_after = tk.Label(frame_path_after, text="移动后路径:")
label_path_after.pack(side=tk.LEFT)

entry_path_after = tk.Entry(frame_path_after, width=40)
entry_path_after.pack(side=tk.LEFT)

button_browse_after = tk.Button(frame_path_after, text="浏览", command=browse_button_path_after)
button_browse_after.pack(side=tk.LEFT)

# 创建关键字输入框
frame_keyword = tk.Frame(window, pady=20)
frame_keyword.grid(row=2, column=0)

label_keyword = tk.Label(frame_keyword, text="关键字:")
label_keyword.pack(side=tk.LEFT)

entry_keyword = tk.Text(frame_keyword, width=40, height=5)
entry_keyword.pack(side=tk.LEFT)

# 创建移动按钮
button_move = tk.Button(window, text="移动文件", command=move_files_by_keywords)
button_move.grid(row=3, column=0)

# 设置窗口在屏幕中居中显示
window.update_idletasks()
width = window.winfo_width()
height = window.winfo_height()
x = (window.winfo_screenwidth() // 2) - (width // 2)
y = (window.winfo_screenheight() // 2) - (height // 2)
window.geometry(f"{width}x{height}+{x}+{y}")

# 启动主窗口的消息循环
window.mainloop()