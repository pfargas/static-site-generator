import unittest
from split_nodes_delimiter import split_nodes_delimiter, split_nodes_image, split_nodes_link
from text_to_textnode import text_to_textnode
from textnode import TextNode, TextType

class TestTextToTextNode(unittest.TestCase):

    def test_basic_formats(self):
        result = text_to_textnode("**Bold** *Italic* `Code`")
        expected = [
            TextNode("Bold", TextType.BOLD),
            TextNode(" ", TextType.TEXT),
            TextNode("Italic", TextType.ITALIC),
            TextNode(" ", TextType.TEXT),
            TextNode("Code", TextType.CODE),
        ]
        self.assertEqual(result, expected)

    def test_only_imge(self):
        result = text_to_textnode("![alt text](https://example.com/image.png)")
        expected = [
            TextNode("alt text", TextType.IMAGE, "https://example.com/image.png"),
        ]
        self.assertEqual(result, expected)

    def test_img_with_unformatted_text(self):
        result = text_to_textnode("Here is an image: ![alt text](https://example.com/image.png) in the text.")
        expected = [
            TextNode("Here is an image: ", TextType.TEXT),
            TextNode("alt text", TextType.IMAGE, "https://example.com/image.png"),
            TextNode(" in the text.", TextType.TEXT),
        ]
        self.assertEqual(result, expected)

    def test_two_nodes(self):
        result = text_to_textnode("This is **bold** and this is an ![image](https://example.com/img.png)")
        expected = [
            TextNode("This is ", TextType.TEXT),
            TextNode("bold", TextType.BOLD),
            TextNode(" and this is an ", TextType.TEXT),
            TextNode("image", TextType.IMAGE, "https://example.com/img.png"),
        ]
        self.assertEqual(result, expected)

    def test_format_and_img_before_and_after(self):
        result = text_to_textnode("**Bold text** before image ![alt](https://example.com/img.png) and *after*.")
        expected = [
            TextNode("Bold text", TextType.BOLD),
            TextNode(" before image ", TextType.TEXT),
            TextNode("alt", TextType.IMAGE, "https://example.com/img.png"),
            TextNode(" and ", TextType.TEXT),
            TextNode("after", TextType.ITALIC),
            TextNode(".", TextType.TEXT),
        ]
        self.assertEqual(result, expected)

    def test_img_and_link(self):
        result = text_to_textnode("Here is an image ![alt](https://example.com/img.png) and a link [click here](https://example.com).")
        expected = [
            TextNode("Here is an image ", TextType.TEXT),
            TextNode("alt", TextType.IMAGE, "https://example.com/img.png"),
            TextNode(" and a link ", TextType.TEXT),
            TextNode("click here", TextType.LINK, "https://example.com"),
            TextNode(".", TextType.TEXT),
        ]
        self.assertEqual(result, expected)

    def test_img_and_link_with_code_formatting(self):
        result = text_to_textnode("`Code before` ![alt](https://example.com/img.png) some text here [link](https://example.com) `Code after`")
        expected = [
            TextNode("Code before", TextType.CODE),
            TextNode(" ", TextType.TEXT),
            TextNode("alt", TextType.IMAGE, "https://example.com/img.png"),
            TextNode(" some text here ", TextType.TEXT),
            TextNode("link", TextType.LINK, "https://example.com"),
            TextNode(" ", TextType.TEXT),
            TextNode("Code after", TextType.CODE),
        ]
        self.assertEqual(result, expected)

    def test_everything_combined(self):
        result = text_to_textnode("**Bold** text with an ![image](https://example.com/img.png), a [link](https://example.com), `code`, **more bold**, and *italic*.")
        expected = [
            TextNode("Bold", TextType.BOLD),
            TextNode(" text with an ", TextType.TEXT),
            TextNode("image", TextType.IMAGE, "https://example.com/img.png"),
            TextNode(", a ", TextType.TEXT),
            TextNode("link", TextType.LINK, "https://example.com"),
            TextNode(", ", TextType.TEXT),
            TextNode("code", TextType.CODE),
            TextNode(", ", TextType.TEXT),
            TextNode("more bold", TextType.BOLD),
            TextNode(", and ", TextType.TEXT),
            TextNode("italic", TextType.ITALIC),
            TextNode(".", TextType.TEXT),
        ]
        self.assertEqual(result, expected)

    def test_bootdev_test(self):
        result = text_to_textnode("This is **text** with an _italic_ word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)")
        expected = [
            TextNode("This is ", TextType.TEXT),
            TextNode("text", TextType.BOLD),
            TextNode(" with an _italic_ word and a ", TextType.TEXT),
            TextNode("code block", TextType.CODE),
            TextNode(" and an ", TextType.TEXT),
            TextNode("obi wan image", TextType.IMAGE, "https://i.imgur.com/fJRm4Vk.jpeg"),
            TextNode(" and a ", TextType.TEXT),
            TextNode("link", TextType.LINK, "https://boot.dev"),
        ]
        self.assertEqual(result, expected)
