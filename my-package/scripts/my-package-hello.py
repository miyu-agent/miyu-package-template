#!/usr/bin/env python3
# Display name: Hello
# 显示名称：打招呼
# Description: Greet someone by name.
# 描述：照名字打个招呼。
# Timeout: 10
# Parameters:
# {"type": "object", "properties": {"name": {"type": "string"}}, "required": ["name"]}

# 上面连着的那一段注释是工具的开头：Description 等几行给模型看（英文短句），描述、显示名称给人看。
# 工具名照文件名（去掉扩展名）：my-package-hello。改编号时文件名一起改，带上编号做前缀免得和别的包撞。
# 参数是一份 JSON，从标准输入读；标准输出、标准错误都交给 AI；退出码不是 0 的算失败，把原因写进输出。
# 写法见 https://github.com/miyu-agent/miyu/blob/main/docs/zh/dev/scripts-skills.md
import json
import sys

args = json.load(sys.stdin)
name = str(args.get("name", "")).strip()
if not name:
    print("name is empty: pass the name of the person to greet.")
    sys.exit(1)
print(f"Hello, {name}!")
