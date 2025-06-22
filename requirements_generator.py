import os
import ast
import pkg_resources
import sys

def find_imports_in_file(filepath):
    with open(filepath, "r", encoding="utf-8") as file:
        node = ast.parse(file.read(), filepath)
    imports = set()
    for n in ast.walk(node):
        if isinstance(n, ast.Import):
            for name in n.names:
                imports.add(name.name.split('.')[0])
        elif isinstance(n, ast.ImportFrom):
            if n.module:
                imports.add(n.module.split('.')[0])
    return imports

def scan_for_imports(path):
    all_imports = set()
    if os.path.isfile(path) and path.endswith(".py"):
        all_imports.update(find_imports_in_file(path))
    elif os.path.isdir(path):
        for root, dirs, files in os.walk(path):
            for file in files:
                if file.endswith(".py"):
                    filepath = os.path.join(root, file)
                    all_imports.update(find_imports_in_file(filepath))
    else:
        print("Invalid file or directory.")
        sys.exit(1)
    return all_imports

def filter_installed_packages(imports):
    installed_packages = {pkg.key for pkg in pkg_resources.working_set}
    result = {}
    for imp in imports:
        if imp.lower() in installed_packages:
            version = pkg_resources.get_distribution(imp).version
            result[imp] = version
    return result

def generate_requirements(path, output_path):
    found_imports = scan_for_imports(path)
    packages = filter_installed_packages(found_imports)
    if not packages:
        print("No external packages found.")
        return
    with open(output_path, "w", encoding="utf-8") as f:
        for package, version in sorted(packages.items()):
            f.write(f"{package}=={version}\n")
    print(f"requirements.txt generated at: {output_path}")

if __name__ == "__main__":
    input_path = input("Enter the absolute path of a Python file or project folder: ").strip().strip('"').strip("'")
    if not os.path.exists(input_path):
        print("The specified path does not exist.")
        sys.exit(1)

    if os.path.isfile(input_path):
        base_dir = os.path.dirname(input_path)
    else:
        base_dir = input_path

    output_file = os.path.join(base_dir, "requirements.txt")
    generate_requirements(input_path, output_file)
