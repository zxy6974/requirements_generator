# 📦 Python Requirements Generator

A simple Python tool that scans a project folder or a single Python file to automatically generate a `requirements.txt` containing all external dependencies (third-party packages with version numbers).

---

## ✨ Features

- 📁 Scan an entire project directory, or
- 📄 Process a single `.py` file
- 📑 Detects all `import` and `from ... import ...` statements
- 📌 Matches found packages with installed packages
- 📝 Creates a clean `requirements.txt` with package versions
- ✅ Ignores Python standard libraries

---

## 📥 Installation

No external dependencies required — uses Python's built-in `ast`, `os`, `pkg_resources`, and `sys` modules.

Python 3.8+ recommended.

```bash
git clone https://github.com/yourusername/requirements-generator.git
cd requirements-generator
python requirements_generator.py
