import unittest
from extract_title import extract_title

class TestExtractTitle(unittest.TestCase):
    
    def test_extract_title_with_title(self):
        markdown = "# My Title\nSome content here."
        self.assertEqual(extract_title(markdown), "My Title")

    def test_extract_title_without_title(self):
        markdown = "No title here.\nJust some content."
        self.assertIsNone(extract_title(markdown))

    def test_extract_title_with_multiple_lines(self):
        markdown = "Introduction line.\n# Another Title\nMore content."
        self.assertEqual(extract_title(markdown), "Another Title")

    def test_extract_title_with_leading_spaces(self):
        markdown = "   # Leading Spaces Title\nContent follows."
        self.assertEqual(extract_title(markdown), "Leading Spaces Title")