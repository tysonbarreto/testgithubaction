from main import get_mode, return_backwards_string
import unittest
import os


class TestMain(unittest.TestCase):
    def test_return_backwards_string(self):
        random_string = "This is my string"
        random_string_reversed = "gnirts tset ym si sihT"
        self.assertEqual(
            random_string,
            return_backwards_string(random_string_reversed)
        )
    
    def test_get_env(self):
        self.assertEqual(os.environ.get('MODE'), get_mode())
        
    
if __name__== "__main__":
    unittest.main()