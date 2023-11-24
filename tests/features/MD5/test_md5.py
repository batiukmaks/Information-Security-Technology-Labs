from features.MD5.md5 import MD5
import unittest

class TestMD5(unittest.TestCase):
    def setUp(self):
        self.md5 = MD5()

    def test_md5_hashes(self):
        test_cases = [
            ("", "d41d8cd98f00b204e9800998ecf8427e"),
            ("The quick brown fox jumps over the lazy dog", "9e107d9d372bb6826bd81d3542a419d6"),
            ("Hello World", "b10a8db164e0754105b7a99be72e3fe5"),
        ]

        for i, (input_data, expected_output) in enumerate(test_cases):
            with self.subTest(test=i):
                self.assertEqual(self.md5.hexdigest(input_data), expected_output)

if __name__ == "__main__":
    unittest.main()