import unittest

from blocktype import BlockType, block_to_block_type

class TestBlockType(unittest.TestCase):
    def test_paragraph(self):
        self.assertEqual(block_to_block_type("This is a simple paragraph."), BlockType.PARAGRAPH)

    def test_heading(self):
        self.assertEqual(block_to_block_type("# This is a heading"), BlockType.HEADING)
        self.assertEqual(block_to_block_type("## This is a subheading"), BlockType.HEADING)

    def test_code(self):
        self.assertEqual(block_to_block_type("```print('Hello, World!')```"), BlockType.CODE)

    def test_quote(self):
        self.assertEqual(block_to_block_type("> This is a quote."), BlockType.QUOTE)

    def test_unordered_list(self):
        self.assertEqual(block_to_block_type("- Item 1"), BlockType.UNORDERED_LIST)
        self.assertEqual(block_to_block_type("- Item 2"), BlockType.UNORDERED_LIST)

    def test_ordered_list(self):
        self.assertEqual(block_to_block_type("1. First item"), BlockType.ORDERED_LIST)
        self.assertEqual(block_to_block_type("2. Second item"), BlockType.ORDERED_LIST)