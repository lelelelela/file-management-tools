# 文件整理工具 / File Management Tools

这个项目包含了一些本人在文件整理时写的一些小工具，以下是每个工具的详细说明：  
This project includes several small tools for file management. Below are detailed descriptions of each tool:

## 运行环境 / Environment
这些脚本可以在Python环境下运行。请确保你已经安装了Python,并在命令行中运行脚本。  
These scripts can run in a Python environment. Please ensure that you have installed Python and run the script from the command line.

## 2. classification.py
**功能**：通过指定关键字，移动路径下（包括子文件夹）的所有包含该关键字的文件到目标路径。  
**Capability**: Moves all files containing the specified keyword within the path (including subdirectories) to the target path.

**操作方式**：图形化操作界面（GUI）。输入一个或多个关键字（使用回车分隔），脚本会依次将匹配的文件移动到目标路径。  
**Operation Method**: Graphical User Interface (GUI). Enter one or more keywords (separated by Enter), and the script will move the matching files to the target path sequentially.

## 4. add_folder_name_front_file.py
**功能**：将文件所在的文件夹名称添加到文件名前，并删除文件所在的子文件夹。  
**Capability**: Adds the folder name to the front of the file name and deletes the subfolder containing the file.

**操作方式**：图形化操作界面（GUI）。运行脚本后，粘贴路径到文本框，点击“移动并重命名文件”，文件名将改为`[子文件夹名]-[原文件名]`，并逐级移动至父文件夹。例如，`文件/报告/年度汇报.docx` 会变为 `文件/报告-年度汇报.docx`。

- **多级目录说明**：如果文件位于多级目录中，点击移动并重命名文件按钮，文件会每点击一次，向上移动一级目录并重命名。例如，如果目标路径是 `D:/File/Documents`，文件将逐级移动，直到到达 `Documents` 文件夹。

**Operation Method**: Graphical User Interface (GUI). After running the script, paste the path into the text box and click “Move and Rename File”. The file name will change to `[Subfolder Name]-[Original File Name]` and move up one level in the directory structure each time the move button is clicked. For example, `Documents/Reports/Annual_Report.docx` will become `Documents/Reports-Annual_Report.docx`.

- **Multilevel Directory Handling**: If the file is in a multilevel directory, each click of the move button will move the file up one level and rename it. For example, if the target path is `D:/File/Documents`, the file will keep moving up until it reaches the `Documents` folder.

## 6. delete_null_path.py
**功能**：自动删除指定路径及其子路径下的所有空文件夹。  
**Capability**: Automatically deletes all empty folders within the specified path and its subpaths.

**操作方式**：图形化操作界面（GUI）。运行脚本后，粘贴路径到文本框，程序将自动删除该路径及子路径下所有的空文件夹

**Operation Method**: Graphical User Interface (GUI). After running the script, paste the path into the text box, and the program will automatically delete all empty folders in the specified path and its subdirectories.

## 9. print_directory_contents.py
**功能**：打印指定目录及其子目录的内容，并显示目录结构。  
**Capability**: Prints the contents of the specified directory and its subdirectories, showing the directory structure.

**操作方式**：无图形化操作界面。通过命令行设置最大递归深度，以控制显示的层级。参数包括：  
**Operation Method**: No Graphical User Interface. The maximum recursion depth can be set via the command line to control the display levels. Parameters include:
- `path`：要打印的目录路径。  
- `path`: The path of the directory to print.
- `depth`：当前递归深度。  
- `depth`: The current recursion depth.
- `max_depth`：最大递归深度。  
- `max_depth`: The maximum recursion depth.
