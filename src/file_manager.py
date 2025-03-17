import os

def create_file(path: str, content: str = ""):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)
    return f"File created at {path}"

def edit_file(path: str, new_content: str):
    if not os.path.exists(path):
        return "File does not exist."
    with open(path, 'w', encoding='utf-8') as f:
        f.write(new_content)
    return f"File updated at {path}"