from pathlib import Path

current_dir = Path.cwd()
current_file = Path(__file__).name

print(f"Files in {current_dir}:")

for filepath in current_dir.iterdir():
    if filepath.name == current_file:
        continue

    print(f"  - {filepath.name}")

    if filepath.is_file():
        try:
            content = filepath.read_text(encoding='utf-8')
        except UnicodeDecodeError:
            content = filepath.read_text(encoding='utf-16')   #добавили из-за проблем с выводом Ты жёстко зашил UTF‑8, а PowerShell создаёт файлы в UTF‑16 LE, поэтому Python падает.


        print(f"    Content: {content}")
