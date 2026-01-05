import os

project_name = os.path.basename(os.getcwd())
files = os.listdir()

content = f"""# {project_name}

## Project Files
"""

for file in files:
    content += f"- {file}\n"

with open("README.md", "w", encoding="utf-8") as f:
    f.write(content)

print("README.md generated successfully")
