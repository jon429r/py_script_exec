import unittest
from py_script_exec import py_run


class TestPyRun(unittest.TestCase):
    def test_valid_script(self):
        exit_code, stdout, _ = py_run("example.py", ["test"])
        self.assertEqual(exit_code, 0)
        self.assertIn("Arguments received", stdout)

    def test_without_extension(self):
        exit_code, stdout, _ = py_run("example", ["test"])
        self.assertEqual(exit_code, 0)
        self.assertIn("Arguments received", stdout)

    def test_script_not_found(self):
        with self.assertRaises(FileNotFoundError):
            py_run("non_existent.py")

    def test_script_not_python(self):
        with self.assertRaises(ValueError):
            py_run("example.txt")

    def test_script_with_error(self):
        exit_code, _, stderr = py_run("error.py", ["error"])
        self.assertNotEqual(exit_code, 0)
        self.assertIn("Error", stderr)

    def test_empty_script_name(self):
        with self.assertRaises(ValueError):
            py_run("")


if __name__ == "__main__":
    unittest.main()
