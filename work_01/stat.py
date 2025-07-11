import os
import ast

def is_python_file(filename):
    return filename.endswith('.py')

def analyze_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        try:
            source = f.read()
        except UnicodeDecodeError:
            return 0, 0, 0  # 跳过无法读取的文件
    try:
        tree = ast.parse(source)
    except SyntaxError:
        return 0, 0, 0  # 跳过语法错误的文件

    class_count = sum(isinstance(node, ast.ClassDef) for node in ast.walk(tree))
    function_count = sum(isinstance(node, ast.FunctionDef) for node in ast.walk(tree))
    line_count = sum(1 for line in source.splitlines() if line.strip() != '')

    return class_count, function_count, line_count

def analyze_folder(folder_path):
    total_classes = 0
    total_functions = 0
    total_lines = 0

    for root, _, files in os.walk(folder_path):
        for file in files:
            if is_python_file(file):
                filepath = os.path.join(root, file)
                c, f, l = analyze_file(filepath)
                total_classes += c
                total_functions += f
                total_lines += l

    print(f'Total classes: {total_classes}')
    print(f'Total functions: {total_functions}')
    print(f'Total lines: {total_lines}')

if __name__ == '__main__':
    import sys
    if len(sys.argv) != 2:
        print("Usage: python analyze_python_files.py <folder_path>")
    else:
        analyze_folder(sys.argv[1])
