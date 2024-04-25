import re

def remove_markdown_lines(filename):
    try:
        # 读取文件内容
        with open(filename, 'r', encoding='utf-8') as file:
            lines = file.readlines()
        
        # 删除包含"#### Page"的行和">"符号
        filtered_lines = [line for line in lines if not re.match(r'^\s*>\s*$', line) and not re.match(r'^\s*#+\s*Page', line)]
        filtered_lines = [re.sub(r'>', '', line) for line in lines]
        # 写回文件
        with open(filename, 'w', encoding='utf-8') as file:
            file.writelines(filtered_lines)
        
        print("Markdown文件处理完成！")
    except Exception as e:
        print("发生错误:", e)

# 用法示例
remove_markdown_lines("c++semi_exam.md")
