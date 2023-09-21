#!/usr/bin/python3
"""Unittest module """
import unittest
import sys
import io
from console import HBNBCommand


class TestConsole(unittest.TestCase):
    """ unittest class for the tests"""
    def setUp(self):
        self.console = HBNBCommand()
        self.stdout = sys.stdout
        self.mock_stdout = io.StringIO()
        sys.stdout = self.mock_stdout

    def tearDown(self):
        sys.stdout = self.stdout
        self.mock_stdout.close()

    def test_show(self):
        """ Test the 'show' command"""
        self.console.onecmd("create User")
        obj_id = self.mock_stdout.getvalue().strip().split()[2][1:-1]
        self.mock_stdout.truncate(0)
        self.console.onecmd(f"show User {obj_id}")
        output = self.mock_stdout.getvalue().strip()
        self.assertTrue(output.startswith("["))


    def test_update(self):
        """ Test the 'update' command"""
        self.console.onecmd("create User")
        obj_id = self.mock_stdout.getvalue().strip().split()[2][1:-1]
        self.mock_stdout.truncate(0)
        self.console.onecmd(f"update User {obj_id} first_name 'John'")
        self.console.onecmd(f"show User {obj_id}")
        output = self.mock_stdout.getvalue().strip()
        self.assertIn("first_name: 'John'", output)

    def test_destroy(self):
        """ Test the 'destroy' command"""
        self.console.onecmd("create User")
        obj_id = self.mock_stdout.getvalue().strip().split()[2][1:-1]
        self.mock_stdout.truncate(0)
        self.console.onecmd(f"destroy User {obj_id}")
        self.console.onecmd(f"show User {obj_id}")
        output = self.mock_stdout.getvalue().strip()
        self.assertEqual(output, "** no instance found **")


if __name__ == '__main__':
    unittest.main()
