import unittest

from hello_copilot.main import greeting


class GreetingTests(unittest.TestCase):
    def test_uses_name(self):
        self.assertIn("Ada", greeting("Ada"))

    def test_blank_name_uses_default(self):
        self.assertIn("learner", greeting("  "))


if __name__ == "__main__":
    unittest.main()
