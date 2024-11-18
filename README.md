# py_script_exec

A Python utility to execute Python scripts with arguments across different operating systems.

## Features

- Run Python scripts programmatically.
- Handles arguments seamlessly.
- Compatible with both `python` and `python3`.

---

## Installation

To use `py_script_exec`, clone the repository and install it locally:

```bash
git clone https://github.com/jon429r/py_script_exec.git
cd py_script_exec
pip install -e .
```

```python
from runner import py_run

# Run a Python script with arguments
exit_code, stdout, stderr = py_run("example.py", ["arg1", "arg2"])

print(f"Exit Code: {exit_code}")
print(f"Output: {stdout}")
print(f"Error: {stderr}")
```

