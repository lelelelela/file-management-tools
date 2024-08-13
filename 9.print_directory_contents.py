import os

def print_directory_contents(path, depth, max_depth, prefix=''):
    if depth > max_depth:
        return
    print(prefix[:-1] + '+--' + os.path.basename(path))
    if os.path.isdir(path):
        for child in os.listdir(path):
            child_path = os.path.join(path, child)
            print_directory_contents(child_path, depth+1, max_depth, prefix + '|  ')

path = r"D:\1.学习"
depth = 0
max_depth = 3
print_directory_contents(path, depth, max_depth, '')