import subprocess
import os
from typing import List, Optional, Tuple
import shutil


def py_run(script_name: str, args: Optional[List[str]] = None) -> Tuple[int, str, str]:
    """
    Runs a Python script with the specified arguments, cross-platform.
    Assumes python python is in the PATH.

    Args:
        script_name (str): The name or path of the Python script to run doesn't need to include .py.
        args (Optional[List[str]]): A list of arguments to pass to the script.

    Returns:
        Tuple[int, str, str]: A tuple containing:
            - The exit code of the script.
            - The standard output of the script.
            - The standard error of the script.
    """
    if script_name == "":
        raise ValueError("Script name cannot be None.")

    # make sure file exenstion is .py
    if not script_name.endswith(".py") and "." in script_name:
        raise ValueError("Script must be a Python script with a .py extension")

    if not script_name.endswith(".py"):
        script_name += ".py"

    if not os.path.exists(script_name):
        raise FileNotFoundError(f"Script '{script_name}' does not exist.")

    # Determine the Python executable to use
    python_executable = "python"
    if not shutil.which("python"):
        python_executable = "python3"

    # Build the command
    command = [python_executable, script_name] + (args if args else [])

    try:
        result = subprocess.run(
            command,
            text=True,
            capture_output=True,
            check=False,
        )
        return result.returncode, result.stdout, result.stderr

    except Exception as e:
        raise RuntimeError(f"Error running script: {e}")
