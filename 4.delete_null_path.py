import os
import tkinter as tk
from tkinter import filedialog, messagebox

def remove_empty_folders(path):
    for root, dirs, files in os.walk(path, topdown=False):
        for dir in dirs:
            dir_path = os.path.join(root, dir)
            if not os.listdir(dir_path):
                print(f"删除空文件夹：{dir_path}")
                os.rmdir(dir_path)

def select_folder():
    folder_path = filedialog.askdirectory()
    entry_folder.delete(0, tk.END)
    entry_folder.insert(tk.END, folder_path)

def clear_empty_folders():
    folder_path = entry_folder.get()
    if not folder_path:
        messagebox.showwarning("警告", "请先选择文件夹！")
        return

    response = messagebox.askyesno("确认", f"确定要清除文件夹 {folder_path} 及其子路径下的所有空文件夹吗？")
    if response == tk.YES:
        try:
            remove_empty_folders(folder_path)
            messagebox.showinfo("成功", "已成功清除空文件夹！")
        except Exception as e:
            messagebox.showerror("错误", f"清除空文件夹时发生错误：{str(e)}")

# 创建主窗口
window = tk.Tk()
window.title("清除空文件夹")
window.geometry("400x150")

# 文件夹选择框
label_folder = tk.Label(window, text="选择文件夹：")
label_folder.pack()
entry_folder = tk.Entry(window, width=40)
entry_folder.pack()

# 清除按钮
button_select = tk.Button(window, text="选择", command=select_folder)
button_select.pack(side=tk.LEFT, padx=5)

button_clear = tk.Button(window, text="清除空文件夹", command=clear_empty_folders)
button_clear.pack(side=tk.LEFT, padx=5, pady=10)

# 运行窗口主循环
window.mainloop()
