"""Test file for testing the main.py file"""

import unittest # for creating the test case
from unittest.mock import patch # for mocking the input
import io # for capturing the output
import sys # for restoring the stdout and removing the main module from the cache
import importlib # for importing the main.py file
from pathlib import Path # for getting the path of the main.py file

class TestMain(unittest.TestCase):
    """Class for testing the main.py file"""

    def setUp(self):
        """Sets up the test environment by removing the main module from the cache"""
        super().setUp()
        sys.modules.pop("main", None)

    @patch("builtins.input", return_value="-1")
    def test_idade_m1(self, _mock_input):
        """Testa se o programa imprime "Impossível!" quando o usuário digita -1"""
        captured_output = io.StringIO()
        sys.stdout = captured_output
        importlib.import_module("main")
        sys.stdout = sys.__stdout__
        self.assertIn("Impossível!", captured_output.getvalue().strip())
        self.assertNotIn("Não precisa se alistar.", captured_output.getvalue().strip())
        self.assertNotIn("Não esqueça de votar na próxima eleição.",
                         captured_output.getvalue().strip())
        self.assertNotIn("Vá descansar.", captured_output.getvalue().strip())
        self.assertNotIn("Eita!", captured_output.getvalue().strip())

    @patch("builtins.input", return_value="0")
    def test_idade_0(self, _mock_input):
        """Testa se o programa imprime "Não precisa se alistar." quando o usuário digita 0"""
        captured_output = io.StringIO()
        sys.stdout = captured_output
        importlib.import_module("main")
        sys.stdout = sys.__stdout__
        self.assertNotIn("Impossível!", captured_output.getvalue().strip())
        self.assertIn("Não precisa se alistar.", captured_output.getvalue().strip())
        self.assertNotIn("Não esqueça de votar na próxima eleição.",
                         captured_output.getvalue().strip())
        self.assertNotIn("Vá descansar.", captured_output.getvalue().strip())
        self.assertNotIn("Eita!", captured_output.getvalue().strip())

    @patch("builtins.input", return_value="17")
    def test_idade_17(self, _mock_input):
        """Testa se o programa imprime "Não precisa se alistar." quando o usuário digita 17"""
        captured_output = io.StringIO()
        sys.stdout = captured_output
        importlib.import_module("main")
        sys.stdout = sys.__stdout__
        self.assertNotIn("Impossível!", captured_output.getvalue().strip())
        self.assertIn("Não precisa se alistar.", captured_output.getvalue().strip())
        self.assertNotIn("Não esqueça de votar na próxima eleição.",
                         captured_output.getvalue().strip())
        self.assertNotIn("Vá descansar.", captured_output.getvalue().strip())
        self.assertNotIn("Eita!", captured_output.getvalue().strip())

    @patch("builtins.input", return_value="18")
    def test_idade_18(self, _mock_input):
        """Testa se o programa imprime "Eita!" quando o usuário digita 18"""
        captured_output = io.StringIO()
        sys.stdout = captured_output
        importlib.import_module("main")
        sys.stdout = sys.__stdout__
        self.assertNotIn("Impossível!", captured_output.getvalue().strip())
        self.assertNotIn("Não precisa se alistar.", captured_output.getvalue().strip())
        self.assertNotIn("Não esqueça de votar na próxima eleição.",
                         captured_output.getvalue().strip())
        self.assertNotIn("Vá descansar.", captured_output.getvalue().strip())
        self.assertIn("Eita!", captured_output.getvalue().strip())

    @patch("builtins.input", return_value="20")
    def test_idade_20(self, _mock_input):
        """Testa se o programa imprime "Não esqueça de votar na próxima eleição."
        quando o usuário digita 20"""
        captured_output = io.StringIO()
        sys.stdout = captured_output
        importlib.import_module("main")
        sys.stdout = sys.__stdout__
        self.assertNotIn("Impossível!", captured_output.getvalue().strip())
        self.assertNotIn("Não precisa se alistar.", captured_output.getvalue().strip())
        self.assertIn("Não esqueça de votar na próxima eleição.",
                      captured_output.getvalue().strip())
        self.assertNotIn("Vá descansar.", captured_output.getvalue().strip())
        self.assertNotIn("Eita!", captured_output.getvalue().strip())

    @patch("builtins.input", return_value="65")
    def test_idade_65(self, _mock_input):
        """Testa se o programa imprime "Eita!" quando o usuário digita 65"""
        captured_output = io.StringIO()
        sys.stdout = captured_output
        importlib.import_module("main")
        sys.stdout = sys.__stdout__
        self.assertNotIn("Impossível!", captured_output.getvalue().strip())
        self.assertNotIn("Não precisa se alistar.", captured_output.getvalue().strip())
        self.assertNotIn("Não esqueça de votar na próxima eleição.",
                         captured_output.getvalue().strip())
        self.assertNotIn("Vá descansar.", captured_output.getvalue().strip())
        self.assertIn("Eita!", captured_output.getvalue().strip())

    @patch("builtins.input", return_value="70")
    def test_idade_70(self, _mock_input):
        """Testa se o programa imprime "Vá descansar." quando o usuário digita 70"""
        captured_output = io.StringIO()
        sys.stdout = captured_output
        importlib.import_module("main")
        sys.stdout = sys.__stdout__
        self.assertNotIn("Impossível!", captured_output.getvalue().strip())
        self.assertNotIn("Não precisa se alistar.", captured_output.getvalue().strip())
        self.assertNotIn("Não esqueça de votar na próxima eleição.",
                         captured_output.getvalue().strip())
        self.assertIn("Vá descansar.", captured_output.getvalue().strip())
        self.assertNotIn("Eita!", captured_output.getvalue().strip())

if __name__ == "__main__":
    # add the parent directory to the path in order to run it from the run command in vscode
    main_file_folder = Path(__file__).parents[1].as_posix() # pylint: disable=invalid-name
    sys.path.insert(0, main_file_folder)
    unittest.main()
