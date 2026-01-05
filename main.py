import os
import sys

def generate_readme(project_path):
    project_name = os.path.basename(project_path)
    files = [
        f for f in os.listdir(project_path)
        if os.path.isfile(os.path.join(project_path, f)) and f != "README.md"
    ]

    content = f"""# {project_name}

## Project Files
"""

    for file in files:
        content += f"- {file}\n"

    readme_path = os.path.join(project_path, "README.md")
    with open(readme_path, "w", encoding="utf-8") as f:
        f.write(content)

    print("README.md generated successfully ✅")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python main.py <project_path>")
    else:
        generate_readme(sys.argv[1])
