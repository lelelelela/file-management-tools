"""
example:
原来文件位于“数一数”文件夹的“学案”文件夹里面，名为“数一数相关知识.doc”
运行程序后，原来的文件改名为“学案-数一数相关知识.doc”，并且取消学案文件夹
改为“数一数”文件夹里面就是“学案-数一数相关知识.doc”
"""


import os
import shutil
import tkinter as tk
from tkinter import filedialog

# def rename_files(path):
#     # 遍历给定路径下的所有文件夹及文件
#     for root, dirs, files in os.walk(path):
#         for file_name in files:
#             if not file_name.startswith('.'):
#                 # 获取文件所在文件夹的名称
#                 folder_name = os.path.basename(root)
#                 file_path = os.path.join(root, file_name)

#                 # 构建新的文件名
#                 new_file_name = f"{folder_name}-{file_name}"
#                 new_file_path = os.path.join(os.path.dirname(root), new_file_name)

#                 # 重命名文件
#                 os.rename(file_path, new_file_path)

def rename_files(path):
    # 获取给定路径下的所有文件夹及文件
    for root, dirs, files in os.walk(path):
        # 遍历文件夹
        for folder_name in dirs:
            folder_path = os.path.join(root, folder_name)

            # 遍历文件夹中的文件
            for file_name in os.listdir(folder_path):
                file_path = os.path.join(folder_path, file_name)

                # 构建新的文件名
                new_file_name = f"{folder_name}-{file_name}"
                new_file_path = os.path.join(path, new_file_name)

                # 移动文件
                shutil.move(file_path, new_file_path)


def remove_empty_folders(path):
    for root, dirs, _ in os.walk(path, topdown=False):
        for dir in dirs:
            dir_path = os.path.join(root, dir)
            if not os.listdir(dir_path):
                print(f"删除空文件夹：{dir_path}")
                os.rmdir(dir_path)


        

def select_directory():
    directory = filedialog.askdirectory()
    path_entry.delete(0, tk.END)
    path_entry.insert(tk.END, directory)

def rename_and_move_files():
    path = path_entry.get()
    if path:
        rename_files(path)
        remove_empty_folders(path)
        result_label.config(text="文件重命名成功并移动")
    else:
        result_label.config(text="请先选择路径")

# 创建图形化界面
root = tk.Tk()
root.title("文件重命名程序")

# 选择路径的部分
path_label = tk.Label(root, text="选择路径：")
path_label.pack()

path_entry = tk.Entry(root, width=50)
path_entry.pack()

select_button = tk.Button(root, text="选择文件夹", command=select_directory)
select_button.pack()

# 重命名和移动的部分
rename_button = tk.Button(root, text="移动并重命名文件", command=rename_and_move_files)
rename_button.pack()

result_label = tk.Label(root, text="")
result_label.pack()

root.mainloop()

