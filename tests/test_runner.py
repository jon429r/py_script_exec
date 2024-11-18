import unittest
from py_script_exec import py_run


class TestPyRun(unittest.TestCase):
    def test_valid_script(self):
        exit_code, stdout, stderr = py_run("example.py", ["test"])
        self.assertEqual(exit_code, 0)
        self.assertIn("Arguments received", stdout)

    def test_script_not_found(self):
        with self.assertRaises(FileNotFoundError):
            py_run("non_existent.py")


if __name__ == "__main__":
    unittest.main()
