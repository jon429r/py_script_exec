# py_script_exec

A Python utility to execute Python scripts with arguments across different operating systems.

## Features

- Run Python scripts programmatically.
- Handles arguments seamlessly.
- Compatible with both `python` and `python3` without changes.

---

## Installation

To use `py_script_exec`, install via pip:

```bash
pip install py_script_exec
```

```python
from py_script_exec import py_run

# Run a Python script with arguments
exit_code, stdout, stderr = py_run("example.py", ["arg1", "arg2"])

print(f"Exit Code: {exit_code}")
print(f"Output: {stdout}")
print(f"Error: {stderr}")
```

